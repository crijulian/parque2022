from django.db import models

class Plazas(models.Model):
    id = models.AutoField(primary_key=True)       
    codigo_plaza = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)  