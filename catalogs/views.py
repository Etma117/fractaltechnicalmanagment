from django.shortcuts import render, HttpResponse, redirect
from .models import Accesorio
from .forms import AccesorioForm, TelefonoForm
from django.contrib import messages
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
def home(request):
    return render(request,'catalogos.html')


class AccesorioListar(LoginRequiredMixin, ListView):
    model = Accesorio
    template_name = 'Accesorio.html'
    context_object_name = 'Accesorio'
    success_url = 'Accesorio'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    

class AccesorioCrearView(LoginRequiredMixin, SuccessMessageMixin, CreateView ):
    model = Accesorio
    template_name = 'crear_Accesorio.html'
    context_object_name = 'Accesorio'
    form_class = AccesorioForm
    success_url = 'Accesorio'
    
    success_message = 'Accesorio Creado...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    permission_required = 'catalogs.create_accesorio'
    raise_exception = True  

   
class AccesorioEditarView(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, UpdateView,):
    model = Accesorio
    template_name = 'crear_Accesorio.html'
    form_class =AccesorioForm
    success_url = reverse_lazy('Accesorio')
    success_message = 'Accesorio actualizado correctamente...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    permission_required = 'catalogs.change_accesorio'
    raise_exception = True  


class AccesorioEliminarView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Accesorio   
    template_name = 'eliminar_Accesorio.html'
    success_message = 'Accesosorio eliminado'
    success_url = reverse_lazy('Accesorio')
    

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    permission_required = 'catalogs.delete_accesorio'
    raise_exception = True  

    #def delete(self, request, *args, **kwargs):
     #   self.object = self.get_object()
      #  self.object.delete()
       # return JsonResponse({'message': 'Accesorio eliminado con éxito'})

    
    

   