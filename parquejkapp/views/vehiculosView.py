
from django.conf                                 import settings
from rest_framework                              import status, views, generics
from rest_framework.response                     import Response
from rest_framework_simplejwt.serializers        import TokenObtainPairSerializer
from rest_framework_simplejwt.backends           import TokenBackend
from rest_framework_simplejwt.exceptions         import TokenError, InvalidToken
#from rest_framework.permisions
from parquejkapp.serializers.vehiculosSerializer import VehiculosSerializer
from parquejkapp.models.vehiculos                import Vehiculos
from parquejkapp.serializers.plazasSerializer    import PlazasSerializer



class VehiculosCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = VehiculosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(serializer.data, status=status.HTTP_201_CREATED)