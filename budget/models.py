from django.db import models
from item.models import Item
from django.urls import reverse


class Budget(models.Model):
    """
    Budget that groups related items. 
    Each budget has items which can be managed. 
    """
    name = models.CharField(max_length=70)
    description = models.TextField()
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('budget:detail', kwargs={self.id})