from django import forms
from .models import Assinatura
from clientes.models import Cliente

class AssinaturaForm(forms.ModelForm):
    clientes = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Temporariamente False para validar manualmente
        label="Clientes"
    )

    class Meta:
        model = Assinatura
        fields = ['nome', 'mensalidade', 'clientes']
        labels = {
            'nome': 'Nome da Assinatura',
            'mensalidade': 'Valor da Mensalidade',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['nome', 'mensalidade']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
        self.fields['clientes'].widget.attrs.update({'class': 'form-check-input'})

    def clean_clientes(self):
        clientes = self.cleaned_data.get('clientes')
        if not clientes:
            raise forms.ValidationError("É obrigatório selecionar ao menos um cliente.")
        return clientes