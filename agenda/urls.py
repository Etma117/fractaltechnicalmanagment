from django.urls import path
from .import views 
from .views import ver_calendario
from .views import EventoListar, EventoCrear, EventoDetailView, EventoUpdateView

urlpatterns = [    
    path('', EventoListar.as_view(), name='agenda'),
    path('agenda', EventoListar.as_view(), name='agenda'),
    path('get_events', views.calendar, name='get_events'),
    path('EventoCrear', EventoCrear.as_view(), name='EventoCrear'),
    path('detalle_evento/<int:pk>/', EventoDetailView.as_view(), name='detalle_evento'),
    path('EventoEditar/<int:pk>/', EventoUpdateView.as_view(), name='EventoEditar'),
    
    #path('detalle_evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),

    path('calendario/', ver_calendario, name='ver_calendario'),
]