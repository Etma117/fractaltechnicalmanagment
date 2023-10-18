from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RefaccionListar, RefaccionCrearView, RefaccionEditarView, RefaccionEliminarView

urlpatterns = [
    path('',views.home, name='home' ),
    path('Refaccion/', RefaccionListar.as_view(), name='Refaccion' ),
    path('RefaccionCrear', RefaccionCrearView.as_view(), name= 'RefaccionCrear'),
    path('RefaccionModificar/<int:pk>/', RefaccionEditarView.as_view(), name="RefaccionEditar"),
    path('RefaccionEliminar/<int:pk>/', RefaccionEliminarView.as_view(), name='RefaccionEliminar')
]

