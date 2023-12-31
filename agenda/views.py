from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import AgendaForm
from django.http import JsonResponse
from django.views import View
from .models import Evento
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
from .models import Evento



class EventoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Evento
    template_name = 'detalle_evento.html'  
    context_object_name = 'evento'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'agenda.view_evento'
    raise_exception = True 

class EventoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Evento
    form_class = AgendaForm
    template_name = 'crear_Accesorio.html'  
    success_url = reverse_lazy('agenda')  
    
    
    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'agenda.change_evento'
    raise_exception = True 



def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    telefono = evento.telefono

   # if telefono.status is not None:
     #   estado_reparacion = telefono.status  # Se obtiene el estado de reparación del teléfono , 
    

    return render(request, 'detalle_evento.html', {'evento': evento, 'telefono': telefono})


def calendar(request):
    all_events = Evento.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'eventos1.html',context)

def ver_calendario(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos1.html', {'eventos': eventos})

def all_events(request):                                                                                                 
    eventos = Evento.objects.all()                                                                                    
    out = []                                                                                                             
    for evento in eventos:                                                                                             
        out.append({                                                                                                     
            'title': evento.tipo_evento,                                                                                         
            'id': evento.id,                                                                                              
            'start': evento.fecha_hora.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
                                                                       
        })                                                                                                               
                                                                                                                     
    return JsonResponse(out, safe=False) 


class EventoListar(ListView):
    model = Evento
    template_name = 'eventos.html' 
    context_object_name = 'evento'
    fields = ['tipo_evento', 'fecha_inicio', 'hora_inicio','hora_termino']
    success_url = 'Eventos'

    def get_queryset(self):
        queryset = self.model.objects.filter(activo = True)
        return queryset
    

class EventoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView, PermissionRequiredMixin):
    model = Evento
    template_name = 'crear_Accesorio.html'
    context_object_name = 'Accesorio'
    form_class = AgendaForm
    success_url = 'agenda'
    
    success_message = 'Evento agendado...'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redireccionamiento  agenda.change_evento

    permission_required = 'agenda.add_evento'
    raise_exception = True 

