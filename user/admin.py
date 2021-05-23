from django.contrib import admin
from .models import User, Skill

# Register your models here.

class SlillsInline(admin.TabularInline):
    model = Skill

class UsersAdmin(admin.ModelAdmin):
    model = User
    inlines = [
        SlillsInline,
    ]

admin.site.register(User, UsersAdmin)