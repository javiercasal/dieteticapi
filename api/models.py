from django.db import models


class Config(models.Model):
    pedido_minimo = models.IntegerField(default=0)
    telefono = models.CharField(max_length=200)

    def __str__(self):
            return 'pedido_min | ' + str(self.pedido_minimo) + ' - tel | ' + self.telefono