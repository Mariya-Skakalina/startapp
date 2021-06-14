from django.db import models
from user.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
import datetime
import redis
import jwt




redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.COOKIES.get('jwt')
        if not username:
            return None
        token = redis_instance.get(username)
        account = None
        try:
            jwt_user = jwt.decode(str(username), settings.SECRET_KEY, algorithms=["HS256"])
            account = User.objects.get(email = jwt_user['email'])
            
        except jwt.ExpiredSignatureError:
            try:
                jwt_user = jwt.decode(token.decode(), settings.SECRET_KEY, algorithms=["HS256"])
                access_token = jwt.encode(
                    {"email": jwt_user['email'],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                    settings.SECRET_KEY,
                    algorithm="HS256"
                )
                redis_instance.set(access_token, token)
                account = User.objects.get(email = jwt_user['email'])
                # account = user
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed("Token not valid")
        # print(account)
        return (account, None)