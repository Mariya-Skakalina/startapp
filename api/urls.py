from django.urls import path
from .views import *

urlpatterns = [
    path('date/', DateOfBirthView.as_view(), name='DateOfBirth'),
    path('skills/', SkillAllView.as_view(), name='skills'),
    path('skill_add/', SkillAddViews.as_view(), name='skill_save'),
    path('delete_skill/<int:pk>', SkillDelete.as_view(), name='delete-skill')
]
