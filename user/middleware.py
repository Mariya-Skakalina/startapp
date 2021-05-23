from django.conf import settings
import datetime
import redis
import jwt
from .models import User


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        print(request.path)
        if '/admin' in request.path:
            
            return response
        else:
            try:
                p = request.COOKIES["jwt"]
                token= redis_instance.get(p)
                try:
                    jwt_user = jwt.decode(str(p), settings.SECRET_KEY, algorithms=["HS256"])
                    user = User.objects.get(email = jwt_user['email'])
                    request.user = user
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
                        request.user = user
                    except jwt.ExpiredSignatureError:
                        request.user = None


            except KeyError:
                token = None
                request.user = None

        
        print(response)

        return response