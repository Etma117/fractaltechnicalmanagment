from django import forms
from django.core.exceptions import ValidationError
from .models import Accesorio, Telefono, Marca
from django.forms import ClearableFileInput
#from django.forms import Button

def es_marca_valida(marca):
        if marca is None:
            return True
        return marca.pk is not None

class AccesorioForm(forms.ModelForm):
    
    nueva_marca = forms.CharField(max_length=100, required=False)
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label='Seleccione una marca')
    
    
    class Meta:
        model = Accesorio
        fields = ['marca', 'nueva_marca' ,'modelo', 'categoria', 'descripcion', 'Cbarras', 'existencias', 'precio', 'preciomayoreo', 'activo', 'imagen'
        ]
        labels={
            'marca': "Marca",
            'nueva_marca' : "Crear Nueva Marca",
            'modelo': "Modelo",
            'categoria': "Categoria",
            'descripcion' : "Descripción",
            'Cbarras': "Código de Barras",
            'existencias' : "Numero de Existencias",
            'precio' : "Precio al Publico",
            'preciomayoreo' : "Precio a Mayoreo o Distribuidores",
            'activo' : "Producto Activo o no Disponible",
            'imagen' : "Imagen para el Accesorio",
        }
        widgets ={
            'marca': forms.Select(attrs={'class': 'form-input'}),
            'nueva_marca' : forms.TextInput(attrs={'class': 'form-input'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-input'}),
            'descripcion' : forms.TextInput(attrs={'class': 'form-control'}),
            'Cbarras':  forms.NumberInput(attrs={'class': 'form-control'}),
            'existencias' : forms.NumberInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'preciomayoreo' : forms.NumberInput(attrs={'class': 'form-control'}),
            'activo' : forms.CheckboxInput(attrs={'class': 'check-input'}),
            'imagen' : forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg', 
                                                       'id':'formFileLg' })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establece el campo 'marca' como requerido
        self.fields['marca'].required = False

    def save(self, commit=True):
        marca = self.cleaned_data.get('marca')
        nueva_marca = self.cleaned_data.get('nueva_marca')

        if nueva_marca:
            # Crea una nueva marca si se proporciona
            marca = Marca.objects.create(nombre=nueva_marca)

        # Configura la marca en el objeto Accesorio
        self.instance.marca = marca

        return super().save(commit)
    
    def clean(self):
        cleaned_data = super().clean()

        # Comprueba si se ha proporcionado una marca válida
        marca = cleaned_data.get('marca')
        nueva_marca = cleaned_data.get('nueva_marca')

        if not marca and not nueva_marca:
            # Si ni la marca ni la nueva_marca están presentes, levanta una excepción de validación
            raise ValidationError('Debe proporcionar una marca.')

        # Comprueba si se ha proporcionado una nueva marca
        if nueva_marca:
            if marca:
                raise ValidationError('No puede proporcionar una nueva marca y seleccionar una marca existente.')

            # Verifica si la nueva marca ya existe en la base de datos
            if Marca.objects.filter(nombre=nueva_marca).exists():
                raise ValidationError('La marca ya existe. Proporcione una nueva marca o seleccione una existente.')

        return cleaned_data
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio

    def clean_preciomayoreo(self):
        preciomayoreo = self.cleaned_data.get('preciomayoreo')
        if preciomayoreo is not None and preciomayoreo < 0:
            raise forms.ValidationError("El precio al mayoreo debe ser un valor positivo.")
        return preciomayoreo
    
       
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__' 
