from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Produto, TipoProduto
from django.contrib.admin import register


@register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")

@register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ("tipo",)
