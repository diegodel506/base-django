from rest_framework.serializers import ModelSerializer

from areas.models import Area

class AreaSerializer(ModelSerializer):
    
    class Meta:
        model = Area
        fields = ['id', 'name']