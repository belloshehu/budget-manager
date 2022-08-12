from django.urls import path
from . import views

app_name = 'sharing'

urlpatterns = [
    path('share-item/<int:pk>/', views.ShareItemView.as_view(), name='share-item'),
    path('share-budget/<int:pk>/', views.ShareBudgetView.as_view(), name='share-budget'),
    path('unshare/<int:pk>/<int:target_user_pk>/', views.ShareDeleteView.as_view(), name='delete'),
]