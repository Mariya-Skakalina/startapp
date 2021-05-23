from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Категория", max_length = 150)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField("Название проекта", max_length = 254)
    description = models.TextField("Описание проекта")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})
