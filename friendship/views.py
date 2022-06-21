from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from .models import Friendship, FriendshipRequest
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

# Friendship Request views

class CreateFriendshipRequest(View):
    """
    View to handle friendship request. 
    """
    model = FriendshipRequest
    template_name = 'friendship/request_list.html'

    def get(self, request, **kwargs):
        """
        Create intance of friendship for a user with matching id. 
        Ensure user does not send more than 1 request.
        """
        # create a friendship instance for a user with matching id
        friend_id = self.kwargs.get('friend_id')
        friend = get_object_or_404(User, id=friend_id)
        friendship = Friendship.objects.create(user=request.user, friend=friend)

        # check if user has an existing request
        friendship_requests = self.get_existing_friendship_requests()
        if friendship and len(friendship_requests)==0  and self.request.user.id != friend_id:
            friend_request = FriendshipRequest.objects.create(friendship=friendship)
        friendship_requests = self.get_friendship_requests()
        return render(
            request,
            self.template_name, 
            {"friend_requests": friendship_requests}
        )

    def get_existing_friendship_requests(self):
        friendship_requests = FriendshipRequest.objects.filter(
            friendship__friend__id=self.kwargs.get('friend_id'),
            friendship__user=self.request.user
        )
        return friendship_requests

    def get_friendship_requests(self):
        """
        Returns all users friendship requests.
        """
        return get_list_or_404(
            FriendshipRequest, 
            friendship__user=self.request.user,
        )


class AcceptFriendshipRequest(View):
    """
    View to handle accepting user friendship request.
    """

    def get(self, request, **kwargs):
        friend_id = self.kwargs.get('friend_id')
        friend = get_object_or_404(User, id=friend_id)
        friendship = self.get_friendship()
        
        # update friendship
        friendship.status = 'AC'
        friendship.save()
        return HttpResponseRedirect( 
            reverse('account:detail', kwargs={'pk':friend_id})
        )

    def get_friendship(self):
        """
        Returns a friendship instance for a friend with matching id.
        """
        return get_object_or_404(
            Friendship, 
            friend__id=self.kwargs.get('friend_id'),
            user=self.request.user
        )
