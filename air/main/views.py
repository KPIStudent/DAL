import datetime
from django.http import HttpResponse
from django.views.generic import View
from .models import Station


class SystemView(View):
    timer = Station.chronology.update_periodicity

    def send_request(self, request):
        if datetime.datetime.now() == self.timer:
            SystemUpdateInfo.update_info(request)

    def get(self, request):
        data = Station.objects.filter(id=request.data['id'])
        return HttpResponse(request, data=data)


class SystemUpdateInfo:

    def update_info(self, request):
        data = request.data
        station = Station(region=data['region'], pollution_percentage=data['pollution_percentage'],
                          allowable_rate=data['allowable_rate'])
        station.save()


class ParametersDepartment:
    def set_regions(self, new_region, station_id):
        return Station.objects.filter(id=station_id).update(region=new_region)

    def del_regions(self, new_region, station_id):
        return Station.objects.filter(id=station_id).delete(region=new_region)

#test

