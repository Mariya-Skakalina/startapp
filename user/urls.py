from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('activate/<slug:slug>/', ActivateUserViews.as_view(), name='is_activate')
]
