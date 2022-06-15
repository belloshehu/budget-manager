from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('', views.ItemCreateView.as_view(), name='create-item'),
    path('list/', views.ItemListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
]