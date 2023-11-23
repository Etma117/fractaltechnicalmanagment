from django import forms
from .models import Accesorio, Telefono, Marca
from django.forms import ClearableFileInput
#from django.forms import Button

class AccesorioForm(forms.ModelForm):
    
    nueva_marca = forms.CharField(max_length=100, required=False)
    
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
            'marca': forms.Select(attrs={'class': 'form-control'}),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Añade un campo de selección para la marca
        marcas = Marca.objects.all()
        self.fields['marca'] = forms.ModelChoiceField(queryset=marcas, empty_label='Seleccione una marca')

    def save(self, commit=True):
        # Guarda el formulario como de costumbre
        obj = super().save(commit=commit)

        # Si se proporciona una nueva marca, crea la marca y asígnala al accesorio
        nueva_marca = self.cleaned_data.get('nueva_marca')
        if nueva_marca:
            marca, created = Marca.objects.get_or_create(nombre=nueva_marca)
            obj.marca = marca
            obj.save()

        return obj
       
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__' 
