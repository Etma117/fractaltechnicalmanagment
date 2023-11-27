from django.contrib import admin
from . models import Accesorio, Categoria, Telefono, Marca
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Accesorio)
admin.site.register(Telefono)

 