from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    """
    Model to represent user's reviews.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"review by {self.user.username}"

