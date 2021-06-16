from django import forms
from django.conf import settings
from rest_framework.fields import DateField


# Форма регистрации
class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)


# Форма авторизации
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
