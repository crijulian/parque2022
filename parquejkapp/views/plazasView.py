
from django.conf                             import settings
from rest_framework                          import generics, status, views
from rest_framework.response                 import Response
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from parquejkapp.serializers.plazasSerializer import PlazasSerializer


class PlazasCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PlazasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
