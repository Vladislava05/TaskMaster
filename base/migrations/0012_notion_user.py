# Generated by Django 3.2.3 on 2021-12-23 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0011_notion'),
    ]

    operations = [
        migrations.AddField(
            model_name='notion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notions', to=settings.AUTH_USER_MODEL),
        ),
    ]