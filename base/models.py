from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from django.utils import timezone


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
