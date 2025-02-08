from django.db import models

class TipoProduto(models.Model):
    TIPO_CHOICES = [
        ('ALI', 'Alimento'),
        ('SOB', 'Sobremesa'),  
        ('ELE', 'Eletrônico'),
    ]

    tipo = models.CharField(
        max_length=3,
        choices=TIPO_CHOICES,
        unique=True,
        default='-',  # Valor padrão alterado para 'O' (Outro)
    )

    def __str__(self):
        return self.get_tipo_display()  # Exibe o valor legível do choice

class Produto(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)  # Removi max_length=1
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome