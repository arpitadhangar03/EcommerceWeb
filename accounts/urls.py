from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

app_name='accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('',TemplateView.as_view(template_name='products/home.html'),name='home'),
    path('profile/',views.profile,name='profile'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    
    # Add other URLs as needed
]