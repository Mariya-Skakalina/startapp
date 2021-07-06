from django.conf import settings
from django.http.request import HttpRequest
from .services import WorkWithToken
from django.http.response import Http404, HttpResponse
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
                    user = User.objects.get(email=jwt_user['email'])
                    request.account = {
                        "id": user.id,
                        "name": user.name,
                        "lastname": user.lastname,
                        "email": user.email,
                        "token": p
                    }
                except jwt.ExpiredSignatureError:
                    try:
                        jwt_user = jwt.decode(token.decode(), settings.SECRET_KEY, algorithms=["HS256"])
                        tks = WorkWithToken(request)
                        user = User.objects.get(email=jwt_user['email'])
                        request.account = {
                            "id": user.id,
                            "name": user.name,
                            "lastname": user.lastname,
                            "email": user.email,
                            "token": tks.update_custom_token(jwt_user, token)
                        }
                    except jwt.ExpiredSignatureError:
                        request.account = None

            except KeyError:
                token = None
                request.account = None
                raise Http404()

    # def process_response(self, request, response):
        # access_token = request.account['token']
        # if access_token:
        #     response.set_cookie("jwt", access_token)
        # return response
