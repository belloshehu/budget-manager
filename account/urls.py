from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf.urls.static import static


app_name = 'account'
urlpatterns = [
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='account/login_form.html'), 
        name='login'
    ),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-friendships/', views.dashboard_friendship, name='friendship'),
    path(
        'dashboard-sent-requests/',
        views.dashboard_sent_friendship_requests, 
        name='sent-requests'
    ),
    path(
        'dashboard-received-requests/',
        views.dashboard_received_friendship_requests, 
        name='received-requests'
    ),
    path(
        'user/<int:pk>/', 
        views.UserDetailView.as_view(), 
        name='detail'
    ),
]
