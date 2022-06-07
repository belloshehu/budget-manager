from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='account/login_form.html'), 
        name='login'
    ),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile')
]