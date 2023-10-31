from django.urls import path
from .import views 
from .views import EventoListar
#from .views import EventoListar

urlpatterns = [    
    path('', views.calendar, name='get_events'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
]