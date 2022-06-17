from django.contrib import admin
from .models import Friendship
# Register your models here.

class FriendshipAdmin(admin.ModelAdmin):
    model = Friendship
    list_display = [
        "user",
        "friend",
        "status",
        "created_at",
        'blocked'
    ]
admin.site.register(Friendship, FriendshipAdmin)


