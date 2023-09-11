from django import forms
from .models import Accesorio
from django.forms import ClearableFileInput

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = '__all__' 
        
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Accesorio
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
