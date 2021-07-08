from django.db import models
from django.urls import reverse

from user.models import User


# Модель категории
class Category(models.Model):
    name = models.CharField("Категория", max_length = 150)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# Модель тегов
class Tag(models.Model):
    name = models.CharField("Тег", max_length=254)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


# Модель проекта
class Project(models.Model):
    name = models.CharField("Название проекта", max_length = 254)
    description = models.TextField("Описание проекта")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="Теги", related_name="tags", blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, default=None, related_name="project_user")
    is_in_search = models.BooleanField("Находится в поиске", default=None, blank=True, null=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.TextField('Описание задачи')
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name
