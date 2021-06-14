from django import forms
from django.conf import settings
from rest_framework.fields import DateField


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)


class DateOfForm(forms.Form):
    age = DateField(input_formats=settings.DATE_INPUT_FORMATS)