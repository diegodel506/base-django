from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from areas.api.serializers import AreaSerializer


from areas.models import Area

class AreaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    

    