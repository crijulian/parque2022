from parquejkapp.models.facturas import Factura
from rest_framework import serializers
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['costo_total', 'tipo_vehiculo','fecha_salida',]