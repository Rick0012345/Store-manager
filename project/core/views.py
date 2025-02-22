from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Produto, TipoProduto
from .forms import ProdutoForm, TipoProdutoForm
from django.urls import reverse_lazy


class BaseView(TemplateView):
    template_name = "vizualizar.html"


class CadastrarProdutoView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/cadastro_produto.html"
    success_url = reverse_lazy("index")

class CadastrarTipoProdutoView(CreateView):
    model = TipoProduto
    form_class = TipoProdutoForm
    template_name = 'produtos/cadastrar_tipo_produto.html'
    success_url = reverse_lazy('index')  # Redireciona para a página inicial