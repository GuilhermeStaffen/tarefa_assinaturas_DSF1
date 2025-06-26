from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'cpf', 'email']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))
