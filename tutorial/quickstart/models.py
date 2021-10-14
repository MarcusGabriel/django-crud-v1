from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_aniversario = models.DateField()
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    data_validade = models.DateField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_venda = models.DateField()
    lista_produtos = models.ManyToManyField(Produto, related_name='vendas')
