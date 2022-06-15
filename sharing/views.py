from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
    fields = ('target_users',)

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
        form.base_fields['target_users'].queryset = active_friends_queryset
        return render(
            request,
            "sharing/share_form.html", 
            {
                'item':item, 
                'form': form,
                'active_friendships': self.get_active_friendships(),
                'target_users': active_friends_queryset
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
        form.instance.user = self.request.user
        form.instance.item = Item.objects.get(id=self.kwargs.get('pk'))
        super().form_valid(form)
        form.instance.target_users.set(User.objects.filter(id__in=form.cleaned_data.get('target_users')))
        return super().form_valid(form)
        

class ShareDeleteView(generic.DeleteView):
    """
    View to unshare item with users.
    """
    model = Share
    context_object_name = 'share'

    def get(self, request, *args, **kwargs):
        print(kwargs.items())
        return super().get(args, kwargs)
        # return render(request, "sharing/share_delete_confirm.html", )

    def get_context_data(self, *args, **kwargs):
        """
        Add target user to the context.
        """
        context = super().get_context_data(*args, **kwargs)
        context['target_user'] = self.get_target_user_object()
        return context

    def get_target_user_object(self):
        """
        Query target user that an item will be unshared with.
        """
        target_user_object = get_object_or_404(
                User, pk=self.kwargs.get('target_user_pk')
        )
        return target_user_object

    def post(self, *args, **kwargs):
        """
        Delete target user from a share. Delete share also there
        is no target user associated with it.
        """
        share = self.get_object()
        item_id = share.item.id
        share.target_users.remove(self.get_target_user_object())
        if len(share.target_users.all()) == 0:
            # remove share instance when no target user is 
            # associated with it.
            share.delete()
        return HttpResponseRedirect(reverse('item:detail', kwargs={'pk': item_id}))
        