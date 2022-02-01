  
from django.db import models
from .user import User


class Facturas(models.Model):
    idfactura = models.AutoField(primary_key=True)    
    costo_total = models.DecimalField(max_digits=5, decimal_places=2,default=0)            
    fecha_salida = models.DateTimeField()  