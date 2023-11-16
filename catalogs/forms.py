from django import forms
from .models import Accesorio, Telefono
from django.forms import ClearableFileInput

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['marca', 'modelo', 'categoria', 'descripcion', 'Cbarras', 'existencias', 'precio', 'preciomayoreo', 'activo', 'imagen'
        ]
        labels={
            'marca': "Marca",
            'modelo': "Modelo",
            'categoria': "Categoria",
            'descripcion' : "Descripción",
            'Cbarras': "Código de Barras",
            'existencias' : "Numero de Existencias",
            'precio' : "Precio al Publico",
            'preciomayoreo' : "Precio a Mayoreo o Distribuidores",
            'activo' : "Producto Activo o Deshabilitado",
            'imagen' : "Imagen para el Accesorio",
        }

       
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__' 
        
"""class ProductoForm2(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['marca', 'nombre', 'categoria', 'modelo', 'descripcion', 'NS', 'existencias', 'precio', 'activo', 'imagen'] #  # se añade , 'imagen' para referenciar a la imagen asosiada

        labels= {
            'marca' : "MARCA",
            'nombre' : "NOMBRE",
            'NS' : "Numero de Serie"
        }

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'NS': forms.NumberInput(attrs={'class': 'form-control'}),
            'existencias': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 0;'}), 
            'imagen': forms.ImageField(widget=ClearableFileInput(attrs={'class': 'form-control'})) 

            widgets ={
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': "Categoria",
            'descripcion' : "Descripción",
            'Cbarras': "Código de Barras",
            'existencias' : "Numero de Existencias",
            'precio' : "Precio al Publico",
            'preciomayoreo' : "Precio a Mayoreo o Distribuidores",
            'activo' : "Producto Activo o Deshabilitado",
            'imagen' : "Imagen para el Accesorio",
        }
        

        }"""

