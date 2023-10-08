from django.contrib import admin
from . models import TipoRefaccion, TipoReparacion, CalidadRefaccion,Refaccion, Reparacion, Status

# Register your models here.
admin.site.register(TipoReparacion)
admin.site.register(TipoRefaccion)
admin.site.register(CalidadRefaccion)
admin.site.register(Refaccion)
admin.site.register(Reparacion)
admin.site.register(Status)
 