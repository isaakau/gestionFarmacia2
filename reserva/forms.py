from django import forms
from .models import *

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

        widgets = {
            "vencimiento": forms.SelectDateWidget()
        }