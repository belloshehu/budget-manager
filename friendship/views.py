from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Friendship
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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
    

class BlockUnblockUserView(generic.UpdateView):
    """
    Block user's friend. Items cannot be shared 
    with blocked users/friends. 
    """
    model = Friendship
    template_name = "friendship/friendship_confirm_block_unblock.html"
    fields = ('blocked',)
    success_url = reverse_lazy('account:friendship')

    def get(self, request, **kwargs):
        return render(
            request, 
            self.template_name,
             {"friendship": self.get_object()}
        )

    def post(self, request, **kwargs):
        object = self.get_object()

        if object.blocked:
            object.blocked = False
        else:
            object.blocked = True
        object.save()
        return HttpResponseRedirect(reverse('account:friendship'))


def friend_search(request):
    """ 
    Searches for a friend with matching or resembling username. 
    """
    users = User.objects.filter(username__icontains = request.GET.get('username'))
    return render(
        request, 
        "search_result.html", 
        {"users": users, "username": request.GET.get('username')}
    )