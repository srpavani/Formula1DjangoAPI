from rest_framework.serializers import ModelSerializer
from ..models import F1ResultModels


class F1ResultSerializer(ModelSerializer):
    class Meta:
        model = F1ResultModels
        fields = ["id", "GrandPix", "data", "vencedor", "time", "voltas"]



