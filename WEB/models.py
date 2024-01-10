from django.db import models

# Create your models here.
class calzado(models.Model):
    #django coloca un id por defecto
    marca   = models.CharField(max_length=40)
    tipo    = models.CharField(max_length=30)
    color   = models.CharField(max_length=30)
    talla   = models.IntegerField()
    genero  = models.CharField(max_length=30)


class indumentaria(models.Model):
    #django coloca un id por defecto
    marca   = models.CharField(max_length=40)
    tipo    = models.CharField(max_length=30)
    color   = models.CharField(max_length=30)
    talla   = models.IntegerField()
    genero  = models.CharField(max_length=30)

class accesorios(models.Model):
    categoria = models.CharField(max_length=40)
    marca     = models.CharField(max_length=40)
    deporte   = models.CharField(max_length=40)