from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetailView.as_view(), name='detailUser'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('activate/<slug:slug>/', ActivateUserViews.as_view(), name='is_activate'),
    path('my_project/', UserMyProject.as_view(), name="my_project")
]
