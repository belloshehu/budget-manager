# Generated by Django 2.2 on 2022-07-03 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0005_friendshiprequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friend',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
