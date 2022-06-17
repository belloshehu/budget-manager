from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Friendship


# Create your views here.
class FriendshipListView(generic.ListView):
    model = Friendship


class UnfriendView(generic.DeleteView):
    """
    Remove a friend from being a user's friend. 
    The user friendship instance with a friend is removed. 
    """
    model = Friendship
    success_url = reverse_lazy('account:friendship')
    