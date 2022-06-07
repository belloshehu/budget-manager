from django.shortcuts import render
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
    

class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'items'




