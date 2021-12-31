from django.db import models
from django.contrib.auth.models import User


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