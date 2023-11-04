from django.db import models
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
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    estado_reparacion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo