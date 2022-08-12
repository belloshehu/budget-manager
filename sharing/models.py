from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Share(models.Model):
    """
    Model to represent instance of sharing item
    with a user.

    This could be ab item that a user wants someone to buy for him. 
    The target user is the person helping the owner. 
    """
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    target_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.item.name} from {self.item.owner.username}"

