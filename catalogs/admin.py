from django.contrib import admin
from . models import Accesorio, Categoria, Telefono,TipoRefaccion, TipoReparacion, CalidadRefaccion,Refaccion, Reparacion
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Accesorio)
admin.site.register(Telefono)
admin.site.register(TipoReparacion)
admin.site.register(TipoRefaccion)
admin.site.register(CalidadRefaccion)
admin.site.register(Refaccion)
admin.site.register(Reparacion)
 