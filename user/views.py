from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from hmac import compare_digest as compare_hash
from django.conf import settings
import datetime
import redis
import crypt
import jwt
from .forms import *
from .models import User

# Create your views here.
class RegisterUserView(CreateView):
    model = User
    template_name = 'user/register.html'
    fields = ['name', 'lastname', 'email', 'password']

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            form = UserRegisterForm()


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class LoginUserView(FormView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])
        if user:
            if compare_hash(user.password, crypt.crypt(str(form.cleaned_data['password']), settings.SECRET_KEY)):
                access_token = jwt.encode(
                    {"email": user.email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                    settings.SECRET_KEY,
                    algorithm="HS256"
                )
                refresh_token = jwt.encode(
                    {"email": user.email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10080)},
                    settings.SECRET_KEY,
                    algorithm="HS256"
                )
                redis_instance.set(access_token, refresh_token)
                response = HttpResponseRedirect('/')
                response.set_cookie("jwt", access_token)
                return response
        return super().form_valid(form)


class ActivateUserViews(TemplateView):
    template_name = 'user/activate.html'

    def get(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
