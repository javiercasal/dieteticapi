from rest_framework import serializers

from .models import Config, Config


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('pedido_minimo', 'telefono')