from django.urls import path
from . import views

app_name = 'sharing'

urlpatterns = [
    path('share/<int:pk>/', views.ShareCreateView.as_view(), name='share'),
    path('unshare/<int:pk>/<int:target_user_pk>/', views.ShareDeleteView.as_view(), name='delete'),
]