from django.contrib import admin

from .models import Task, UserProfile

admin.site.register(Task)
admin.site.register(UserProfile)
