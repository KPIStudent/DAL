from rest_framework import serializers
from .models import Station, Chronology


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class ChronologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chronology
        fields = '__all__'

