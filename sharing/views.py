from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Share
from item.models import Item
from .forms import ShareForm
from django.contrib.auth.models import User
from friendship.models import Friendship

# Create your views here.
class ShareCreateView(generic.CreateView):
    """
    View to allow user to share item with another user.
    """
    model = Share
    fields = ('target_user',)

    def get_success_url(self, *args, **kwargs):
        return reverse('item:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        form = self.get_form_class()

        # get user queryset for active friends
        active_friends_queryset = User.objects.filter(
            id__in=self.get_active_friends_ids()
        ).exclude(id__exact=request.user.id)

        # set the select options by overiding the queryset
        # property of the form 
        form.base_fields['target_user'].queryset = active_friends_queryset
        return render(
            request,
            "sharing/share_form.html", 
            {
                'item':item, 
                'form': form,
                'active_friendships': self.get_active_friendships()
            }
        )
    
    def get_active_friendships(self):
        """
        Returns user's friends whom are not blocked.
        """
        active_friendships = Friendship.objects.filter(status__iexact='AC', blocked=False)
        return active_friendships

    def get_active_friends_ids(self):
        """
        Returns the list of active friends ids
        """
        friends_ids = [ friendship.friend.id for friendship in self.get_active_friendships()]
        return friends_ids
    
    def form_valid(self, form):
        print(self.request.POST['target_user'])
        form.instance.user = self.request.user
        form.instance.target_user = User.objects.get(id=self.request.POST.get('target_user'))
        form.instance.item = Item.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)
        

class ShareDeleteView(generic.DeleteView):
    """
    View to unshare item with users.
    """
    model = Share
