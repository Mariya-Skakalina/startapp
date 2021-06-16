from django import forms
from .models import Category


# Добавление проекта
class ProjectAddForm(forms.Form):
    name = forms.CharField(max_length=500, required=True)
    description = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
