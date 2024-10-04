from django.db import models
from django.utils import timezone

class Productoo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    cantidadStock = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)