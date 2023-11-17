from django import forms
from .models import Refaccion, TipoRefaccion, TipoReparacion, CalidadRefaccion, Reparacion

from django.forms import ClearableFileInput

class RefaccionForm(forms.ModelForm):
    class Meta:
        model = Refaccion
        fields = ['marca', 'modelos', 'tipo_de_pieza', 'calidad_refaccion', 'existencias',
                   'precio', 'preciomayoreo']
        labels= {
            'marca' : "Marca",
            'modelo' : "Modelo o modelos",
            'tipo_de_pieza' : "Tipo de refacion",
            'calidad_refaccion' : "Calidad de la Refacion",
            'existencias': "Existencias",
            'precio': "Precio a publico",
            'preciomayoreo': "Precio a Mayoristas o Socios" 
        }
        widgets ={
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelos': forms.TextInput(attrs={'class': 'form-control'}), #multiple Choices
            'tipo_de_pieza': forms.Select(attrs={'class': 'form-control'}),
            'calidad_refaccion': forms.Select(attrs={'class': 'form-control'}),
            'existencias' : forms.NumberInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'preciomayoreo' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = '__all__'

class TipoRefaccionForm(forms.ModelForm):
    class Meta:
        model = TipoRefaccion
        fields = '__all__' 

class TipoReparacionForm(forms.ModelForm):
    class Meta:
        model = TipoReparacion
        fields = '__all__' 

class CalidadRefaccionForm(forms.ModelForm):
    class Meta:
        model = CalidadRefaccion
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
        }"""

