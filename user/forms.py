from django import forms


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
