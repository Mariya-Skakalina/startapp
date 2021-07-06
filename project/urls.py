from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>', ProjectDetailView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('add/', ProjectAddView.as_view(), name='add_project'),
    path('<pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('<pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
]
