from django.urls import path
from .views import ProjectList,ProjectDeleteView

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>', ProjectDeleteView.as_view())
]
