from django.db import models


class Stands(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.localizacao} - R${self.valor}'


class Reserva(models.Model):
    CATEGORIA_CHOICES = (
        ('artesanato', 'Artesanato'),
        ('livraria', 'Livraria'),
        ('fast-food', 'Fast-Food')
    )
    stand = models.OneToOneField(
        Stands, on_delete=models.SET_NULL, null=True
    )
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES
    )
    cnpj = models.CharField(max_length=18)
    quitado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome_empresa
