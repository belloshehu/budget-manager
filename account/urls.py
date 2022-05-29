from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'account/login/', 
        auth_views.LoginView.as_view(template_name='account/login_form.html'), 
        name='login'
    )
]