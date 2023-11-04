# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Refaccion, TipoRefaccion, TipoReparacion, CalidadRefaccion, Reparacion

from .forms import RefaccionForm
from django.contrib import messages
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
def home(request):
    return render(request,'catalogs.html')


class RefaccionListar(LoginRequiredMixin, ListView):
    model = Refaccion
    template_name = 'refaccion_list.html' 
    context_object_name = 'Refaccion'
    success_url = 'Refaccion'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    

class RefaccionCrearView(LoginRequiredMixin, SuccessMessageMixin, CreateView ):
    model = Refaccion
    template_name = 'crear_Refaccion.html' #crear tempaltre*/*/*
    context_object_name = 'Refaccion'
    success_url = 'Refaccion'
    form_class = RefaccionForm
       
    success_message = 'Refaccion registrada...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    #permission_required = 'catalogs.create_accesorio'
    raise_exception = True  

   
class RefaccionEditarView(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, UpdateView,):
    model = Refaccion
    template_name = 'crear_Refaccion.html'
    form_class =RefaccionForm
    success_url = reverse_lazy('Refaccion')
    success_message = 'Refacion actualizada correctamente...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    permission_required = 'repairlab.change_refaccion'
    raise_exception = True  


class RefaccionEliminarView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Refaccion  
    template_name = 'eliminar_Refaccion.html'
    success_message = 'Refacion dada de baja'
    success_url = reverse_lazy('Refaccion')
    

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento

    permission_required = 'repairlab.delete_refaccion'
    raise_exception = True  

    #def delete(self, request, *args, **kwargs):
     #   self.object = self.get_object()
      #  self.object.delete()
       # return JsonResponse({'message': 'Accesorio eliminado con éxito'})

    
    
