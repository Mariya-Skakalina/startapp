import datetime
import jwt

from django.conf import settings
from .models import User


def creating_token(user: User, time: int) -> str:
    """"Создание токена"""
    token = jwt.encode(
        {"email": user,
         "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=time)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    return token
