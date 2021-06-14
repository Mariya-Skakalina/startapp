from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>', ProjectDeleteView.as_view()),
    path('category/<int:pk>', CategoryDeleteView.as_view()),
    path('add/', ProjectAddView.as_view(), name='add_project')
]
