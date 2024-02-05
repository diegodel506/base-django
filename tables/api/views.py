from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from tables.api.serializers import TableSerializer

from tables.models import Table


class TableApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TableSerializer
    queryset = Table.objects.all().order_by("number")
    # Filtros...
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["area", "id", "number"]
