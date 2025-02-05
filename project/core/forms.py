from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = self.fields['preco']
        field.widget.attrs.update({'class': 'form-control form-preco'})