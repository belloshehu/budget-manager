from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Share
from item.models import Item
from .forms import ShareForm
from django.contrib.auth.models import User
from friendship.models import Friendship
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from .utils  import send_email, get_target_users_email
from budget.models import Budget


class ShareItemView(LoginRequiredMixin, generic.CreateView):
    """
    View to allow user to share item with another user.
    """
    model = Share
    fields = ('target_users',)
    shared_model = Item # model of the item/budget to be shared
    email_subject = "Sharing Item"
    template_name = 'sharing/share_item_form.html'
    item_key = "item"

    def get_success_url(self, *args, **kwargs):
        return reverse('item:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        form = self.get_form_class()

        # get user queryset for active friends
        active_friends_queryset = get_user_model().objects.filter(
            id__in=self.get_active_friends_ids()
        ).exclude(id__exact=request.user.id)

        # set the select options by overiding the queryset
        # property of the form 
        form.base_fields['target_users'].queryset = active_friends_queryset
        return render(
            request,
            self.template_name, 
            {
                self.item_key:self.get_shared_object(), 
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
    
    def add_instance_properties(self, form):
        """
        Defines user, target_users and content_object
        properties of the Share Model instance.
        """
        form.instance.user = self.request.user
        # form.instance.item = Item.objects.get(id=self.kwargs.get('pk'))
        form.instance.content_object = self.get_shared_object()
        # super().form_valid(form)
        target_users = get_user_model().objects.filter(id__in=form.cleaned_data.get('target_users'))
        form.instance.target_users.set(target_users)
        form.save()

    def form_valid(self, form): 
        self.add_instance_properties(form)

        context = {
            "item": self.get_shared_object(),
            "request": self.request
        }
        # send email notification
        send_email(
            self.email_subject,
            get_target_users_email(target_users),
            self.get_shared_object(),
            context,
            "sharing/email/share_notification.html"
        )
        return super().form_valid(form)

    def get_shared_object(self):
        """
        Returns item to be shared
        """
        return get_object_or_404(self.shared_model, id=self.kwargs.get('pk'))
        

class ShareBudgetView(ShareItemView):
    """
    View for sharing Budget with friends.
    """
    model = Share
    shared_model = Budget
    email_subject = "Sharing Budget"
    template_name = 'sharing/share_budget_form.html'
    item_key = "budget"


class ShareDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    View to unshare item with users.
    """
    model = Share
    context_object_name = 'share'

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
                get_user_model(), pk=self.kwargs.get('target_user_pk')
        )
        return target_user_object

    def post(self, *args, **kwargs):
        """
        Delete target user from a share. Delete share also there
        is no target user associated with it.
        """
        share = self.get_object()
        item_id = share.item.id
        try:
            target_user = self.get_target_user_object()
            share.target_users.remove(self.get_target_user_object())
            context = {
                "item": share.item,
                "request": self.request
            }
            # send email notification
            send_email(
                "Unsharing Item",
                [target_user.email],
                share.item,
                context,
                "sharing/email/unshare_notification.html"
            )
        except Exception as e:
            print(f'Error: { e}')

        if len(share.target_users.all()) == 0:
            # remove share instance when no target user is 
            # associated with it.
            share.delete()
        return HttpResponseRedirect(reverse('item:detail', kwargs={'pk': item_id}))
        