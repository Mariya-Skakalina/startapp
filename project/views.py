from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import ProjectAddForm
from .models import Project, Category


# Вывести все проекты
class ProjectList(ListView):
    model = Project
    template_name = 'project/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        context['categories'] = Category.objects.all()
        return context


# Вывести один проект
class ProjectDeleteView(DetailView):
    model = Project
    template_name = "project/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        return context


# Отфильтровать проекты по категориям
class CategoryDeleteView(DetailView):
    model = Category
    template_name = 'project/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        context['projects'] = Project.objects.filter(category = self.kwargs['pk'])
        context['categories'] = Category.objects.all()
        return context


# Добавление проекта
class ProjectAddView(CreateView):
    model = Project
    template_name = 'project/add_project.html'
    fields = ['name', 'description', 'category']

    def post(self, request, *args, **kwargs):
        form = ProjectAddForm(request.POST)
        if form.is_valid():
            Project.objects.create(**form.cleaned_data, author = request.account)
            return HttpResponseRedirect('/')
        else:
            form = ProjectAddForm()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.account
        return context
