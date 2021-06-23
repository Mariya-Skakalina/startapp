from user.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
import redis
import jwt

from user.services import WorkWithToken

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


# Пользовательская проверка аунтефикации
class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.COOKIES.get('jwt')
        if not username:
            return None
        token = redis_instance.get(username)
        account = None
        try:
            jwt_user = jwt.decode(str(username), settings.SECRET_KEY, algorithms=["HS256"])
            account = User.objects.get(email=jwt_user['email'])
            
        except jwt.ExpiredSignatureError:
            try:
                jwt_user = jwt.decode(token.decode(), settings.SECRET_KEY, algorithms=["HS256"])
                tks = WorkWithToken(request)
                tks.update_custom_token(jwt_user, token)
                account = User.objects.get(email=jwt_user['email'])
                # account = user
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed("Token not valid")
        # print(account)
        return (account, None)