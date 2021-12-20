from django.db import models
from django.contrib.auth.models import User
from django.forms.fields import ImageField
from django.utils import timezone


from django.dispatch import receiver

from django.conf import settings
from django.urls.base import reverse


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['due_date']

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return str(self.user)