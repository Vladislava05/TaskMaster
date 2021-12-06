from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls.base import reverse


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    

    class Meta:
        ordering=['due_date']


def validate_image_size(image):
    file_size = image.file.size
    max_image_size = settings.MAX_IMAGE_SIZE
    if file_size > max_image_size:
        raise ValidationError("maximum picture size should not be more than 2MB")


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", validators=[validate_image_size], null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={'username':self.user.username})


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.profile.save()
        
      
        
        
       
