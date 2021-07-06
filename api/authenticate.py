import jwt

from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings

from user.models import User
from user.services import WorkWithToken


# Пользовательская проверка аунтефикации
class ExampleAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        tks = WorkWithToken(request)
        redis_instance = tks.redis_instance
        username = request.COOKIES.get('jwt')
        if not username:
            return None
        token = redis_instance.get(username)
        try:
            jwt_user = jwt.decode(str(username), settings.SECRET_KEY, algorithms=["HS256"])
            account = User.objects.get(email=jwt_user['email'])
            
        except jwt.ExpiredSignatureError:
            try:
                jwt_user = jwt.decode(token.decode(), settings.SECRET_KEY, algorithms=["HS256"])

                tks.update_custom_token(jwt_user, token)
                account = User.objects.get(email=jwt_user['email'])
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed("Token not valid")

        return (account, None)