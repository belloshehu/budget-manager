# Generated by Django 2.2 on 2022-06-11 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0002_auto_20220611_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PN', 'PENDING'), ('RE', 'REJECTED'), ('AC', 'ACCEPTED')], default='PENDING', max_length=50)),
                ('friendship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendship.Friendship')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
