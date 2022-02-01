from django.db import models
from .plazas import Plazas

class Vehiculos(models.Model):
    id    = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=30)
    tipo_vehiculo = models.CharField(max_length=30) 
    id_plazask = models.ForeignKey(Plazas, related_name='plaza', on_delete=models.CASCADE)  
    fecha_entrada = models.DateTimeField()