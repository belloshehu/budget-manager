from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from reviews.models import Review
from item.models import Item
from friendship.models import Friendship
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import utils
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'custom_account/profile.html')


def home(request):
    reviews = Review.objects.all()[:3]
    return render(request, "home.html", {"reviews": reviews})

@login_required
def dashboard(request):
    return render(request, "custom_account/dashboard_item.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_friendship(request):
    return render(request, "custom_account/dashboard_friendship.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_sent_friendship_requests(request):
    return render(request, "custom_account/dashboard_sent_requests.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_received_friendship_requests(request):
    return render(
        request,
        "custom_account/dashboard_received_requests.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_budgets(request):
    return render(
        request, 
        "custom_account/dashboard_budget.html",
        utils.get_dashboard_contents(request)
    )

class UserList(generic.ListView):
    model = get_user_model()


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = 'custom_account/user_detail.html'