
from rest_framework                          import generics
from parquejkapp.models.user                import User
from parquejkapp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserOtherAccounts(generics.ListAPIView):
    serializer_class   = UserSerializer
    def get_queryset(self):
        queryset = User.objects.exclude(id=self.kwargs['user_id'])
        return queryset


class UserUpdateView(generics.UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)