from django import forms
from .models import Evento

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['tipo_evento', 'telefono', 'titulo', 'descripcion', 'fecha_inicio','fecha_termino','hora_inicio','hora_termino'] 
        labels = {
            'tipo_evento' : "Tipo de Evento",
            'telefono': "Telefono a reparar",
            'titulo' : "Titulo",
            'descripcion': "Descripción",
            'fecha_inicio' : "Fecha",            
            'fecha_termino' : "Fecha de Termino",
            'hora_inicio' : "Hora de inicio",
            'hora_termino' : "Hora de termino"

        }
        widgets = {
            'tipo_evento': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'hora_inicio' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),            
            'hora_termino' : forms.TimeInput(attrs={'class': 'form-control', 'type':'time'})
            
        }