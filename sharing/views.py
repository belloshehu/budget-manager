from django.shortcuts import render
from django.views import generic

# Create your views here.

class ShareCreateView(generic.CreateView):
    """
    View to allow user to share item with another user.
    """
    model = Share
    