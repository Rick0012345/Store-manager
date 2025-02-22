from django.forms import ModelForm
from .models import Produto, TipoProduto
from django import forms

class ProdutoForm(ModelForm):
    tipo = forms.ModelChoiceField(  # Alterado para ModelChoiceField
        queryset=TipoProduto.objects.all(),
        empty_label="Selecione um tipo"
    )

    class Meta:
        model = Produto
        fields = ['tipo', 'nome', 'preco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione classes Bootstrap a todos os campos
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TipoProdutoForm(ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['tipo']