from django.urls import path
from . import views

urlpatterns = [
    path('stations/station/', views.StationView.as_view()),
    path('stations/station/<int:station_id>/', views.StationByIdView.as_view()),
    path('chronology/', views.ChronologyView.as_view()),
    path('chronology/<int:chronology_id>/', views.ChronologyByIdView.as_view())
]