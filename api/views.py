from rest_framework import viewsets

from .serializers import ConfigSerializer
from .models import Config


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all().order_by('telefono')
    serializer_class = ConfigSerializer