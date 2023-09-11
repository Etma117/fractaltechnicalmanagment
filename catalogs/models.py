from django.db import models

# Create your models here.
class Accesorio(models.Model):
    marca = models.CharField(max_length=20)
    modelo= models.CharField(max_length=40)
    categoria = models.CharField(max_length=20)
    descripcion= models.CharField(max_length = 100)
    Cbarras = models.CharField(max_length=20, null=False)

    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)

class Telefono(models.Model):
    marca = models.CharField(max_length=20)
    modelo= models.CharField(max_length=40)
    descripcion= models.CharField(max_length = 100)
    IMEI = models.CharField(max_length=20, null=False)

    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)