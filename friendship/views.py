from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from .models import Friendship, FriendshipRequest
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
# email import :
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .utils import send_email


# Create your views here.
class FriendshipListView(generic.ListView):
    model = Friendship


class UnfriendView(generic.DeleteView):
    """
    Remove a friend from being a user's friend. 
    The user friendship instance with a friend is removed. 
    """
    model = Friendship
    success_url = reverse_lazy('custom_account:friendship')
    

class BlockUnblockUserView(generic.UpdateView):
    """
    Block user's friend. Items cannot be shared 
    with blocked users/friends. 
    """
    model = Friendship
    template_name = "friendship/friendship_confirm_block_unblock.html"
    fields = ('blocked',)
    success_url = reverse_lazy('custom_account:friendship')

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
        return HttpResponseRedirect(reverse('custom_account:friendship'))


def friend_search(request):
    """ 
    Searches for a friend with matching or resembling username. 
    """
    users = get_user_model().objects.filter(
        username__icontains = request.GET.get('username')
    )
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
        friend = get_object_or_404(get_user_model(), id=friend_id)
        friendship = Friendship.objects.create(user=request.user, friend=friend)

        # check if user has an existing request
        friendship_requests = self.get_existing_friendship_requests()
        if friendship and len(friendship_requests)==0  and self.request.user.id != friend_id:
            try:
                friend_request = FriendshipRequest.objects.create(friendship=friendship)
    
                # send email notification to the target friend:
                # friend to whom request is sent
                receiver = friend_request.friendship.friend
                context = {
                    'friendship_request': friend_request,
                    'request': self.request,
                    'site_name': 'Errand',
                    'receiver_username': receiver.username,
                    'friend': friend_request.friendship.user
                }
                send_email(
                    "Friend Request",
                    [receiver.email],
                    friend_request,
                    context,
                    "friendship/email/request_notification.html"
                )
            except Exception as e:
                print(f'Error: {e}')
        friendship_requests = self.get_friendship_requests()
        return HttpResponseRedirect(
            reverse('custom_account:sent-requests')
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
    Email notification is sent to the user who made the request.
    """

    def get(self, request, **kwargs):
        friend_id = self.kwargs.get('friend_id')
        friend = get_object_or_404(get_user_model(), id=friend_id)
        friendship = self.get_friendship()
        
        # update friendship
        friendship.status = 'AC'
        friendship.save()

        # send email notification to the request isuer:
        # friend to whom request was sent
        friend_request = get_object_or_404(
            FriendshipRequest, 
            friendship__id=friendship.id
        )
        friend = friend_request.friendship.friend
        context = {
            'friendship_request': friend_request,
            'request': self.request,
            'site_name': 'Errand',
            'receiver_username': friend_request.friendship.user.username,
            'friend': friend
        }
        send_email(
            "Request Accepted",
            [friendship.user.email],
            friend_request,
            context,
            "friendship/email/request_accepted.html"
        )
        return HttpResponseRedirect( 
            reverse('custom_account:detail', kwargs={'pk':friend_id})
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
    

