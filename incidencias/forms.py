
from django import forms
from .models import Incidencia


class IncidenciaForm(forms.ModelForm):

    class Meta:
        model = Incidencia
        fields = [
            "tipo",
            "categoria",
            "titulo",
            "descripcion",
            "prioridad",
            "fecha_compromiso",
        ]

        labels = {
            "tipo": "Tipo de registro",
            "categoria": "Categoría",
            "titulo": "Título del reporte",
            "descripcion": "Descripción detallada",
            "prioridad": "Prioridad",
            "fecha_compromiso": "Fecha compromiso",
        }

        widgets = {
            "tipo": forms.Select(attrs={
                "class": "form-select"
            }),
            "categoria": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. Sistema, impresora, red, mantenimiento"
            }),
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Escribe un título breve"
            }),
            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe el problema o actividad pendiente"
            }),
            "prioridad": forms.Select(attrs={
                "class": "form-select"
            }),
            "fecha_compromiso": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }
