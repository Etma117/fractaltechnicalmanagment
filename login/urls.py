from django.urls import path
from django.contrib.auth import views as auth_views
from login.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('logout/', auth_views. LogoutView.as_view(next_page='login.html'), name='logout'),
]