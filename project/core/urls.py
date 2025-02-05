from django.contrib import admin
from django.urls import path
from .views import BaseView, CadastrarProdutoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='index'),
    path('cadastro/', CadastrarProdutoView.as_view(), name='cadastro'),
]
