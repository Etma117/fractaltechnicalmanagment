from django.db import models

# Create your models here.
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
    
class Status(models.Model):        ##Status para los diferentes modelso que lo requiera
    estado = models.CharField(max_length=100)
    def __str__(self):
        return self.estado
    
class Refaccion(models.Model):      #modelorefacion
    marca = models.CharField(max_length=20, null=True, blank=True)
    modelos= models.CharField(max_length=40, null=True, blank=True)
    tipo_de_pieza= models.ForeignKey(TipoRefaccion, on_delete=models.CASCADE)
    calidad_refaccion= models.ForeignKey(CalidadRefaccion, on_delete=models.CASCADE)
    
    existencias= models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)

    activo = models.BooleanField(default=True, null=True, blank=True) #añadir status -> pendiente, en proceso, terminado, entregado
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.modelos
        

class Reparacion(models.Model): #modeloReparacion
    tipo_de_reparacion= models.ForeignKey(TipoReparacion, on_delete=models.CASCADE)
    refaccion= models.ForeignKey(Refaccion, on_delete=models.CASCADE,null=True, blank=True) #usar un buscador

    nombreCliente= models.CharField(max_length=20, null=True)
    appCliente= models.CharField(max_length=20, null=True) #Apellido paterno
    apm= models.CharField(max_length=20, null=True) #Apellido materno

    marca = models.CharField(max_length=20, null=True, blank=True)
    modelo= models.CharField(max_length=40,null=True, blank=True)  
    IMEI= models.CharField(max_length=40,null=True, blank=True)   
    año= models.CharField(max_length=40)   
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1) #pendiente, en proceso, terminado, entregado
    
    def __str__(self):
        return self.modelo
    
    def save(self, *args, **kwargs):
        if self.precio == 0.0:
            if self.refaccion:
                # Obtener los costos de tipo_de_reparacion y refaccion
                costo_tipo_reparacion = self.tipo_de_reparacion.mano_de_obra
                costo_refaccion = self.refaccion.precio

                # Calcular el precio total
                precio_total = costo_tipo_reparacion + costo_refaccion

                # Asignar el precio total al campo "precio"
                self.precio = precio_total
            else:
                costo_tipo_reparacion = self.tipo_de_reparacion.mano_de_obra
                self.precio=costo_tipo_reparacion
            
        super().save(*args, **kwargs)