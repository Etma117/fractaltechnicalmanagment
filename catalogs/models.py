from django.db import models

# Create your models here.
class Categoria(models.Model):  ##Categoria de Accesorios
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Accesorio(models.Model):  ##ModeloAccesorios
    marca = models.CharField(max_length=20)
    modelo= models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length = 100)
    Cbarras = models.CharField(max_length=20, null=False)

    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)
 
    def __str__(self):
        return self.modelo

class Telefono(models.Model):    ##ModeloTelefonos en venta
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
    
    def __str__(self):
        return self.modelo
    
class TipoRefaccion(models.Model):      ##Tipos de refaciones (Display, centros de carga, bocinas, etc)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class TipoReparacion(models.Model):         ##Tipos de reparacion a realizar (Display, centros de carga, bocinas, etc) -> precios en un estandar
    nombre = models.CharField(max_length=100)
    mano_de_obra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.nombre
    
class CalidadRefaccion(models.Model):        ##Calidad de la refaccion, a mejor calidad mayor el precio (No influye en la mano de obra)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Refaccion(models.Model):      #modelorefacion
    marca = models.CharField(max_length=20, null=True, blank=True)
    modelos= models.CharField(max_length=40, null=True, blank=True)
    tipo_de_pieza= models.ForeignKey(TipoRefaccion, on_delete=models.CASCADE)
    calidad_refaccion= models.ForeignKey(CalidadRefaccion, on_delete=models.CASCADE)
    
    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)

    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.modelos
        

class Reparacion(models.Model): #modeloReparacion
    tipo_de_reparacion= models.ForeignKey(TipoReparacion, on_delete=models.CASCADE)
    refaccion= models.ForeignKey(Refaccion, on_delete=models.CASCADE) #usar un buscador

    marca = models.CharField(max_length=20, null=True, blank=True)
    modelo= models.CharField(max_length=40,null=True, blank=True)  
    año= models.CharField(max_length=40)   
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.modelo
    
    def save(self, *args, **kwargs):
        # Obtener los costos de tipo_de_reparacion y refaccion
        costo_tipo_reparacion = self.tipo_de_reparacion.mano_de_obra
        costo_refaccion = self.refaccion.precio

        # Calcular el precio total
        precio_total = costo_tipo_reparacion + costo_refaccion

        # Asignar el precio total al campo "precio"
        self.precio = precio_total

        super().save(*args, **kwargs)
