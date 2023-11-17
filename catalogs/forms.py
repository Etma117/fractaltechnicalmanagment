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
        widgets ={
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class': 'form-control'}),
            'Cbarras':  forms.NumberInput(attrs={'class': 'form-control'}),
            'existencias' : forms.NumberInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'preciomayoreo' : forms.NumberInput(attrs={'class': 'form-control'}),
            'activo' : forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'imagen' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

       
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__' 
