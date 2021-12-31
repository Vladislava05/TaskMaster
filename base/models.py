from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import ImageField

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Notion(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notions',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notions')