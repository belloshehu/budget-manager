# Generated by Django 2.2 on 2022-08-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
