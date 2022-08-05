from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from budget.models import Budget


class Comment(models.Model):
    """
    What users discuss about item.
    """
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"comment by {self.user.username}"


class Item(models.Model):
    """
    Model to represent Item that a user want to acquire/buy
    directly or indirectly.
    """
    name = models.CharField(max_length=150)
    description = models.TextField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    done = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='items')
    accepted = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.name