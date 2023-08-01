from django import forms
from .models import Feedback, TipoConsulta, Contacto

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields= '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_consulta'].queryset = TipoConsulta.objects.all()

class contactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields='__all__'
        


