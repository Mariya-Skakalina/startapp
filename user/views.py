from django.views.generic import CreateView, FormView, TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from hmac import compare_digest as compare_hash
from project.models import Project
import redis
import crypt

from .forms import *
from .models import User
from .services import WorkWithToken


# Регистрация пользователя
class RegisterUserView(CreateView):
    model = User
    template_name = 'user/register.html'
    fields = ['name', 'lastname', 'email', 'password']

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        else:
            form = UserRegisterForm()


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


# Авторизация пользователя
class LoginUserView(FormView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        return context

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])
        if user:
            if compare_hash(user.password, crypt.crypt(str(form.cleaned_data['password']), settings.SECRET_KEY)):
                token = WorkWithToken(self.request)
                return token.write_token_in_cookies(user)
            else:
                return HttpResponseRedirect('/user/login')
        return super().form_valid(form)


# Активация почты
class ActivateUserViews(TemplateView):
    template_name = 'user/activate.html'

    def get(self, request, *args, **kwargs):
        print(request)


# Личная информация пользователя
class UserDetailView(DetailView):
    model = User
    template_name = "user/detail.html"

    def get_context_data(self, *args, **kwargs):
        kwargs['account'] = self.request.account
        context = super().get_context_data(**kwargs)
        return context


# Список всех пользователей
class UserList(ListView):
    model = User
    template_name = 'user/all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        return context


# Список всех проектов пользователя
class UserMyProject(ListView):
    model = Project
    template_name = 'user/user_projects.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        return context

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.account)
