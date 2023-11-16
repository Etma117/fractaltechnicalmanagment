from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AccesorioListar, AccesorioCrearView, AccesorioEditarView, AccesorioEliminarView

urlpatterns = [
    path('',views.home, name='home' ),
    path('accesorios/', AccesorioListar.as_view(), name='accesorios' ),
    path('AccesorioCrear', AccesorioCrearView.as_view(), name= 'AccesorioCrear'),
    path('AccesorioModificar/<int:pk>/', AccesorioEditarView.as_view(), name="AccesorioEditar"),
    path('AccesorioEliminar/<int:pk>/', AccesorioEliminarView.as_view(), name='AccesorioEliminar')
]

