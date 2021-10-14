from django.db import transaction
from rest_framework import serializers

from tutorial.quickstart.models import Usuario, Categoria, Produto, Venda


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    preco_final = serializers.FloatField(read_only=True)

    class Meta:
        model = Venda
        fields = ['id', 'comprador', 'data_venda', 'lista_produtos', 'preco_final']

    def create(self, validated_data):
        print(validated_data)
        preco_final = 0
        for produto in validated_data['lista_produtos']:
            preco_final += produto.preco
        venda = Venda(comprador=validated_data['comprador'], data_venda=validated_data['data_venda'],
                      preco_final=preco_final)
        venda.save()
        for produto in validated_data['lista_produtos']:
            print(produto)
            venda.lista_produtos.add(Produto.objects.get(pk=produto.pk))

        return venda
