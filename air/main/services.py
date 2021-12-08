from .models import Station, Chronology
from .serializers import StationSerializer, ChronologySerializer


def get_stations(request):
    if 'allowable_rate' in request.GET:
        return Station.objects.filter(allowable_rate=request.GET[0]['allowable_rate'])
    return Station.objects.all()


def get_station_by_id(station_id):
    return Station.objects.filter(id=station_id)


def get_chronology():
    return Chronology.objects.all()


def get_chronology_by_id(chronology_id):
    return Chronology.objects.filter(id=chronology_id)


class Adapter:
    @staticmethod
    def serialize_station(data):
        return StationSerializer(data, many=True)

    @staticmethod
    def serialize_chronology(data):
        return ChronologySerializer(data, many=True)