from django.urls import path
from .views import *

urlpatterns = [
    path('date/', DateOfBirthView.as_view(), name='DateOfBirth')
]