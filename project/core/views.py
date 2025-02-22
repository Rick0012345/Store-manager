from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Produto, TipoProduto
from .forms import ProdutoForm, TipoProdutoForm
from django.urls import reverse_lazy
from django.http import JsonResponse

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
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Salva o novo tipo de produto
        self.object = form.save()
        # Retorna uma resposta JSON para requisições AJAX
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'id': self.object.id,
                'tipo': self.object.tipo,
            })
        return super().form_valid(form)

    def form_invalid(self, form):
        # Retorna erros de validação para requisições AJAX
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            }, status=400)
        return super().form_invalid(form)