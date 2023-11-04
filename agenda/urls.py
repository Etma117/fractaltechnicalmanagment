from django.urls import path
from .import views 
from .views import EventoListar
#from .views import EventoListar

urlpatterns = [    
<<<<<<< HEAD
        path('', EventoListar.as_view(), name='agenda'),
    path('get_events', views.calendar, name='get_events'),


    path('detalle_evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
=======
    path('', views.calendar, name='get_events'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
>>>>>>> f5970b05e91c326a39132e186826ca99bfe9a73a
]