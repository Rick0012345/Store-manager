from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Produto
from django.contrib.admin import register
# Register your models here.
@register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')