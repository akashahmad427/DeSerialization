from rest_framework import serializers
from .models import Data
class Serializerdata(serializers.Serializer):
    name = serializers.CharField(max_length=80)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=90)
    def create(self, validated_data):
        return Data.objects.create(**validated_data)
    
    