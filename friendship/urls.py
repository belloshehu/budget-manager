from django.urls import path
from . import views

app_name = 'friendship'

urlpatterns = [
    path(
        'unfriend/<int:pk>/', 
        views.UnfriendView.as_view(), 
        name='unfriend'
    ),
    path(
        'block/<int:pk>/',
        views.BlockUnblockUserView.as_view(),
        name='block'
    ),
    path(
        'search/',
        views.friend_search,
        name='search'
    )
]