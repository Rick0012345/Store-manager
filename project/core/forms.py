from django.forms import ModelForm
from .models import Produto, TipoProduto
from django import forms


class ProdutoForm(ModelForm):
    tipo = forms.ChoiceField(choices=TipoProduto.TIPO_CHOICES)

    class Meta:
        model = Produto
        fields = ["tipo", "nome", "preco"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = self.fields["preco"]
        field.widget.attrs.update({"class": "form-control form-preco"})
