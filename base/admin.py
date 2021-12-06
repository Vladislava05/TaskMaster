from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Task, UserProfile

admin.site.register(Task)
admin.site.register(UserProfile)
