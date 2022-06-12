from django.db import models
from django.conf import settings

# Create your models here.
class Friendship(models.Model):
    """
    Model to represent relationship between users. Only users with friendship 
    can share item among themselves.
    """
    REQUEST_STATUS = (
        ('PN', 'PENDING'),
        ('RE', 'REJECTED'),
        ('AC', 'ACCEPTED')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    created_at = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=REQUEST_STATUS, default='PENDING')

    def __str__(self):
        return f" Friendship with {self.friend.username}"
    
    def save(self, *args, **kwargs):
        if self.user.id == self.friend.id:
            raise ValueError("sender and receiver can't be the same")
        return super().save(*args, **kwargs)


# class FriendshipRequest(models.Model):
#     """
#     Model to represent friendship request 
#     sent to from one user to another.
#     """
#     REQUEST_STATUS = (
#         ('PN', 'PENDING'),
#         ('RE', 'REJECTED'),
#         ('AC', 'ACCEPTED')
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=REQUEST_STATUS, default='PENDING')
#     friendship = models.ForeignKey(Friendship, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.status} request."

#     class Meta:
#         ordering = ["created_at"]