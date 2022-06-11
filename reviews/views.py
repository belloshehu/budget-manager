from django.shortcuts import render
from django.contrib.views import generic
from django.contrib.mixins import LoginRequiredMixin
from reviews.models import Review

# Create your views here.

class ReviewCreateView(, generic.CreateView):
    model = Review


class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Review
