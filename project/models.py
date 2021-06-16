from django.db import models
from user.models import User, Skill


# Модель категории
class Category(models.Model):
    name = models.CharField("Категория", max_length = 150)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# Модель проекта
class Project(models.Model):
    name = models.CharField("Название проекта", max_length = 254)
    description = models.TextField("Описание проекта")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    teg = models.ManyToManyField(Skill, verbose_name="Теги", related_name="tags", blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, default=None, related_name="project_user")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})
