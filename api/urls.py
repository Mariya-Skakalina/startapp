from django.urls import path
from .view_all.user_views import DateOfBirthView
from .view_all.base_views import BaseAddViews, BaseAllView, BaseDelete
from .views import *

urlpatterns = [
    path('date/', DateOfBirthView.as_view(), name='DateOfBirth'),
    path('skills/<int:pk>/', SkillAllView.as_view(), name='skills'),
    path('skill_add/', SkillAddViews.as_view(), name='skill_save'),
    path('delete_skill/<int:pk>/<int:id_project>/', SkillDelete.as_view(), name='delete-skill'),
    path('tags/<int:pk>/', BaseAllView.as_view()),
    path('tag_add/', BaseAddViews.as_view(), name='skill_save'),
    path('delete_tag/<int:pk>/<int:id_project>/', BaseDelete.as_view())
]
