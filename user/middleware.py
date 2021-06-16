from django.conf import settings
from django.http.request import HttpRequest
import datetime
from django.http.response import Http404
import redis
import jwt
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
from .models import User


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request: HttpRequest):
        request.account = None
        current_url = resolve(request.path_info).url_name
        auth_list = ['detailUser']
        if '/admin' in request.path or '/user/register/' in request.path or '/user/login/' in request.path:
            return 
        else:
            try:
                p = request.COOKIES.get('jwt')
                if not p and current_url in auth_list:
                    raise Http404()
                elif not p:
                    return
                token = redis_instance.get(p)
                try:
                    jwt_user = jwt.decode(str(p), settings.SECRET_KEY, algorithms=["HS256"])
                    user = User.objects.get(email = jwt_user['email'])
                    request.account = user
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
                        user = User.objects.get(email = jwt_user['email'])
                        request.account = user
                    except jwt.ExpiredSignatureError:
                        request.account = None

            except KeyError:
                token = None
                request.account = None
                raise Http404()