
import datetime
import jwt
from typing import Union

import redis
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import User


def _create_token(jwt_user: Union[User, dict], time: int) -> str:
    if isinstance(jwt_user, User):
        user = {
            "name": jwt_user.name,
            "lastname": jwt_user.lastname,
            "email": jwt_user.email,
        }
    elif isinstance(jwt_user, dict):
        user = {
            "name": jwt_user['name'],
            "lastname": jwt_user['lastname'],
            "email": jwt_user['email'],
        }
    else:
        user = {}

    user["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
    token = jwt.encode(user, settings.SECRET_KEY, algorithm="HS256")
    return token


class WorkWithToken:

    def __init__(self, request):
        self.redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
        self.request = request

    def write_user_to_redis(self, access_token: str, refresh_token: str) -> str:
        self.redis_instance.set(access_token, refresh_token)
        return access_token

    def write_token_in_cookies(self, user) -> HttpResponseRedirect:
        access_token = _create_token(jwt_user=user, time=1)
        refresh_token = _create_token(jwt_user=user, time=1000)
        self.write_user_to_redis(access_token, refresh_token)
        response = HttpResponseRedirect('/')
        response.set_cookie("jwt", access_token)
        return response

    def update_custom_token(self, user: dict, token: str) -> str:
        access_token = _create_token(jwt_user=user, time=30)
        self.write_user_to_redis(access_token, token)
        return access_token
