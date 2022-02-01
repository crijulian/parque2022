from parquejkapp.models.vehiculos import Vehiculos
from parquejkapp.models.plazas import Plazas
from rest_framework import serializers
from parquejkapp.serializers.plazasSerializer import PlazasSerializer

class VehiculosSerializer(serializers.ModelSerializer):    
    class Meta:
        plazas = PlazasSerializer()
        model = Vehiculos
        fields = ['id','placa', 'tipo_vehiculo','id_plazask','fecha_entrada']
    
 
    def to_representation(self, obj):
        #idplazask= Plazas(read_only=True, many=True)
        plaza = Plazas.objects.get(id=obj.id_plazask_id)
        vehiculos = Vehiculos.objects.get(id=obj.id)

        return {
                    'id': vehiculos.id,
                    'placa': vehiculos.placa,
                    'tipo_vehiculo': vehiculos.tipo_vehiculo,
                    'id_plazask': {
                        'id': plaza.id,
                        'codigo_plaza': plaza.codigo_plaza,
                        },
                    'fecha_entrada':vehiculos.fecha_entrada,
                    
                }