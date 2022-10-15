from rest_framework import serializers

from .models import Config, Producto


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('pedido_minimo', 'telefono')


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'detalle', 'marca', 'imagen', 'imagenes', 'url', 'precio',
                  'cantidad', 'unidad', 'plural', 'conStock', 'oferta', 'mostrarDetalle', 'tags', 'rating')
