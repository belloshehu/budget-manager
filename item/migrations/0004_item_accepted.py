# Generated by Django 2.2 on 2022-06-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
    ]
