from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic 
from item.models import Item
from item.forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import send_email, get_target_users_email


# Create your views here.

class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    """
    View to handle request for creating Item.
    """
    model = Item
    form_class = ItemForm
    template_name = "item/item_form.html"
    success_url = reverse_lazy('custom_account:dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    
class ItemDetailView(generic.DetailView):
    model = Item

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class ItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Item

    def post(self, request, *args, **kwargs):
        # send email:
        item = self.get_object()
        context = {
            "item": item,
            "request": self.request
        }
        target_users = self.get_target_users(item)
        # send email notification
        send_email(
            "Item Deleted",
            get_target_users_email(target_users),
            item,
            context,
            "item/email/delete_notification.html"
        )
        return super().post(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return reverse('custom_account:dashboard')

    def get_target_users(self, item):
        """
        Get users/friends that an item was shared with.
        """
        sharing_queryset = item.share_set.all().filter(item__id=item.id)
        target_users =sharing_queryset[0].target_users.get_queryset()
        return target_users


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'items'


class ItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item_update.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('item:detail', kwargs={'pk': self.kwargs.get('pk')})
