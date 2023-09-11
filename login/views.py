from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mainpage.html'
    login_url = 'login'

def home(request):
    return render (
        request,
        'base.html'
    )