from rest_framework import viewsets

from .serializers import ConfigSerializer, ProductoSerializer
from .models import Config, Producto


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all().order_by('telefono')
    serializer_class = ConfigSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('rating')
    serializer_class = ProductoSerializer
