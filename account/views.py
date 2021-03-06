from django.shortcuts import render, reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from reviews.models import Review
from item.models import Item
from friendship.models import Friendship
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import utils
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(password1, password2)
            form.save(commit=True)
            return HttpResponseRedirect(reverse('account:login'))
        return render(request, 'account/signup_form.html', {'form':form})
        # if form.is_valid():
        #     form.clean()
        #     password1 = form.cleaned_data.get('password1')
        #     password2 = form.cleaned_data.get('password2')

        #     if password1 != password2:
        #         message(request, 'Password did not match')
        #         return render(request, 'account/signup_form.html', {'form':form})
        #     form.save()
        #     return HttpResponseRedirect(reverse('account:login'))
    else:
        return render(request, 'account/signup_form.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'account/profile.html')


def home(request):
    reviews = Review.objects.all()[:3]
    return render(request, "home.html", {"reviews": reviews})

@login_required
def dashboard(request):
    return render(request, "account/dashboard_item.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_friendship(request):
    return render(request, "account/dashboard_friendship.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_sent_friendship_requests(request):
    return render(request, "account/dashboard_sent_requests.html", 
        utils.get_dashboard_contents(request)
    )

@login_required
def dashboard_received_friendship_requests(request):
    return render(request, "account/dashboard_received_requests.html", 
        utils.get_dashboard_contents(request)
    )


class UserList(generic.ListView):
    model = User


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'account/user_detail.html'