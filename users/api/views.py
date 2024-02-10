from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django.views.decorators.csrf import csrf_exempt

# from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.hashers import make_password


from users.models import User
from users.api.serializers import UserSerializer


@csrf_exempt
class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return super().create(request, *args, **kwargs)

    # Override de la contraseña de usuario
    def partial_update(self, request, *args, **kwargs):
        password = request.data["password"]
        if password:
            request.data["password"] = make_password(password)
        else:
            request.data["password"] = request.user.password
        return super().update(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Usuario autenticado: ", request.user)

        serializer = UserSerializer(request.user)
        return Response(serializer.data)
