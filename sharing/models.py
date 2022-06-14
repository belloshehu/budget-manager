from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Share(models.Model):
    """
    Model to represent instance of sharing item
    with a user.

    This could be ab item that a user wants someone to buy for him. 
    The target user is the person helping the owner. 
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    target_users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item.name} from {self.item.owner.username}"

