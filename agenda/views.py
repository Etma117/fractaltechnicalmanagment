from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse

# Create your views here.
from .models import Evento

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    telefono = evento.telefono
    estado_reparacion = telefono.status  # Se obtiene el estado de reparación del teléfono , 

    return render(request, 'detalle_evento.html', {'evento': evento, 'telefono': telefono, 'estado_reparacion': estado_reparacion})


def calendar(request):
    all_events = Evento.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'eventos1.html',context)

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

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Evento(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Evento.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Evento.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


class EventoListar(ListView):
    model = Evento
    template_name = 'eventos.html' 
    context_object_name = 'evento'
    fields = ['tipo_evento', 'fecha_hora', 'horario']
    success_url = 'Eventos'