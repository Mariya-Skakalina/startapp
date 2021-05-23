from django.db import models

# Создание пользователя
class User(models.Model):
    name = models.CharField("Имя", max_length=50)
    lastname = models.CharField("Фамилия", max_length = 150)
    age = models.DateField("Дата рождения", null=True, blank=True)
    email = models.EmailField("Электронная почта", max_length=254, unique=True)
    abouth_self = models.TextField("О себе", blank=True, null=True)
    password = models.CharField("Пароль", max_length=50)
    code_activate = models.CharField(max_length=20, default='')
    is_activation = models.BooleanField("Активный", default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Skill(models.Model):
    name = models.CharField("Навык", max_length = 150)
    user_skills = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
