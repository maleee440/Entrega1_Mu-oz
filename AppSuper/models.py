from django.db import models

# Create your models here.

class Cajero(models.Model):
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    camada = models.IntegerField()

class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()
    
class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()
    precio = models.IntegerField()
  