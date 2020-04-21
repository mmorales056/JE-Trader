from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    fecha_inicio = models.CharField(max_length=100)
    fecha_fin = models.CharField(max_length=100)
    estado = models.BooleanField(default = True)

class Dia(models.Model):
    fecha = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    inversion = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    divisa = models.CharField(max_length=100,default="")
    total = models.FloatField(default=0)



class Noche(models.Model):
    fecha = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    inversion = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    divisa = models.CharField(max_length=100, default="")
    total = models.FloatField(default=0)

