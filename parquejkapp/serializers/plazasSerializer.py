  
from parquejkapp.models.plazas import Plazas
from rest_framework import serializers

class PlazasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plazas
        fields = ['id','codigo_plaza', 'estado']

    def to_representation(self, obj):
        plazas = Plazas.objects.get(id=obj.id)        
        return {
                    'id': plazas.id,
                    'codigo_plaza': plazas.codigo_plaza,
                    'estado': plazas.estado,                    
                    
                }