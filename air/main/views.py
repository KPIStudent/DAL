from rest_framework.views import Response
from rest_framework.views import APIView
from .services import *
from .fabric import StationUpdate, ChronologyUpdate
from .serializers import StationSerializer, ChronologySerializer


class StationView(APIView):
    def get(self, request):
        stations = get_stations(request)
        if not stations:
            return Response(f"No station yet")
        station_serializer = Adapter.serialize_station(stations)
        return Response(station_serializer.data)

    def post(self, request):
        data = request.data
        serializer = StationSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(f"New station was added")
        return Response(serializer.errors)


class StationByIdView(APIView):
    def get(self, request, station_id):
        station = get_station_by_id(station_id)
        if not station:
            return Response(f"No station with id={station_id}")
        serializer = Adapter.serialize_station(station)
        return Response(serializer.data)

    def put(self, request, station_id):
        data = request.data
        station = get_station_by_id(station_id)
        if not station:
            return Response(f"No station with id={station_id}")
        StationUpdate().update_model(station, data)
        return Response(f"Station with id={station_id} was updated")

    def delete(self, request, station_id):
        station = get_station_by_id(station_id)
        station.delete()
        return Response(f"Station with id={station_id} was deleted")


class ChronologyView(APIView):
    def get(self, request):
        chronology = get_chronology()
        if not chronology:
            return Response(f"No station yet")
        chronology_serializer = Adapter.serialize_chronology(chronology)
        return Response(chronology_serializer.data)

    def post(self, request):
        data = request.data
        chronology = ChronologySerializer(data=data, many=True)
        if chronology.is_valid():
            chronology.save()
            return Response(f"New station was added")
        return Response(chronology.errors)


class ChronologyByIdView(APIView):
    def get(self, request, chronology_id):
        chronology = get_chronology_by_id(chronology_id)
        if not chronology:
            return Response(f"No station with id={chronology_id}")
        serializer = Adapter.serialize_chronology(chronology)
        return Response(serializer.data)

    def put(self, request, chronology_id):
        data = request.data
        chronology = get_chronology_by_id(chronology_id)
        if not chronology:
            return Response(f"No station with id={chronology_id}")
        ChronologyUpdate().update_model(chronology, data)
        return Response(f"Station with id={chronology_id} was updated")

    def delete(self, request, chronology_id):
        chronology = get_chronology_by_id(chronology_id)
        chronology.delete()
        return Response(f"Station with id={chronology_id} was deleted")
