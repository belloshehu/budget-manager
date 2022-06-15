from django.shortcuts import render
from django.urls import reverse
from django.views import generic 
from item.models import Item
from item.forms import ItemForm

# Create your views here.

class ItemCreateView(generic.CreateView):
    """
    View to handle request for creating Item.
    """
    form_class = ItemForm
    model = Item
    template_name = "item/item_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    
class ItemDetailView(generic.DetailView):
    model = Item

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class ItemDeleteView(generic.DeleteView):
    model = Item

    def get_success_url(self, *args, **kwargs):
        return reverse('account:dashboard')


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'items'




