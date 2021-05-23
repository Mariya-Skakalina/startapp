from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.
class ProjectList(ListView):
    model = Project
    template_name = 'project/main.html'

class ProjectDeleteView(DetailView):
    model = Project
    template_name = "project/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    