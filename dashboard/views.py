from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html' 
    login_url = 'login'  # URL de inicio de sesión (si no se proporciona, se usará el valor predeterminado)
    
