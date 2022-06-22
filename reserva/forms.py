from django import forms
from .models import *

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

        widgets = {
            "vencimiento": forms.SelectDateWidget()
        }

class RutPacienteForm(forms.Form):
    class Meta:
        model = Paciente
        fields = ['rutPaciente']

class AsignarPacienteForm(forms.Form):
    rutPaciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
    observacion = forms.CharField(max_length=200, help_text="Ingrese observaciones e indicaciones para el paciente")
