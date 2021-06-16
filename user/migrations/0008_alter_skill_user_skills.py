# Generated by Django 3.2 on 2021-06-14 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210517_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user_skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_user', to='user.user', verbose_name='Пользователь'),
        ),
    ]
