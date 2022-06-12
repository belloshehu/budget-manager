from django.shortcuts import render
from django.views import generic
from .models import Friendship


# Create your views here.
class FriendshipListView(generic.ListView):
    model = Friendship
    