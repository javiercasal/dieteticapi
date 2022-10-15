from email.policy import default
from pyexpat import model
from django.db import models


class Config(models.Model):
    pedido_minimo = models.IntegerField(default=0)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return 'pedido_min-' + str(self.pedido_minimo) + ' tel-' + self.telefono


class Producto(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    nombre = models.CharField(max_length=200)
    detalle = models.TextField(default='', blank=True)
    marca = models.CharField(max_length=200, default='', blank=True)
    imagen = models.CharField(max_length=255)
    imagenes = models.TextField()
    url = models.CharField(max_length=255, default='', blank=True)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=1)
    unidad = models.CharField(max_length=200)
    plural = models.CharField(max_length=200, default='', blank=True)
    conStock = models.BooleanField(default=True)
    oferta = models.BooleanField(default=False)
    mostrarDetalle = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, default='', blank=True)
    rating = models.IntegerField()

    def __str__(self):
        marca = ''
        if (self.marca):
            marca = '"' + self.marca + '"'
        return str(self.id) + ' | ' + str(self.nombre) + ' ' + marca
