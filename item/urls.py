from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('item/<int:budget_id>/', views.ItemCreateView.as_view(), name='create'),
    path('list/', views.ItemListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
]