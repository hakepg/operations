from rest_framework.serializers import ModelSerializer
from .models import Sample

class sampleSerializer(ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'