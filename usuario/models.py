from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    longitud = models.CharField(max_length=30)
    latitud = models.CharField(max_length=30)
    estadogeo = models.CharField(max_length=30)