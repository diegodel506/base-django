from rest_framework.serializers import ModelSerializer

from areas.api.serializers import AreaSerializer
from tables.models import Table


class TableSerializer(ModelSerializer):
    area_data = AreaSerializer(source="area", read_only=True)

    class Meta:
        model = Table
        fields = ["id", "number", "area", "area_data"]
