from django.db import models
from django.utils import timezone
from repairlab.models import Reparacion

# Create your models here.
class Evento(models.Model):
    TIPOS_DE_EVENTO = (
        ('Reparacion', 'Reparación'),
        ('Inventario', 'Inventario'),
        ('ReunionPersonal', 'Reunión de Personal'),
    )

    tipo_evento = models.CharField(max_length=15, choices=TIPOS_DE_EVENTO)
    telefono = models.ForeignKey(Reparacion, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_termino = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(auto_now=False, auto_now_add=False,default=0, null= True, blank=True)
    hora_termino= models.TimeField(auto_now=False, auto_now_add=False,default=0, null= True, blank=True)
    estado_reparacion = models.CharField(max_length=40, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
