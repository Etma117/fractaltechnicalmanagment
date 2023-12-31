from django.db import models

# Create your models here.
class Categoria(models.Model):  ##Categoria de Accesorios
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    """
    INSERT INTO catalogs_categoria (nombre) VALUES 
  ('Estuches y Fundas'),
  ('Protectores de Pantalla'),
  ('Cargadores y Cables'),
  ('Auriculares y Altavoces'),
  ('Soportes y Monturas'),
  ('Baterías Externas'),
  ('Accesorios de Fotografía'),
  ('Adaptadores y Convertidores'),
  ('Accesorios de Audio y Micrófonos'),
  ('Misceláneos');

    """
class Marca(models.Model):  ##Marcas para Accesorios
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Accesorio(models.Model):  ##ModeloAccesorios
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo= models.CharField(max_length=40, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length = 100)
    Cbarras = models.CharField(max_length=20, null=False)

    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    preciomayoreo = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, null=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)

    imagen = models.ImageField( upload_to="accesorios/", default='accesorios/default.png', null=True, blank=True)
 
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