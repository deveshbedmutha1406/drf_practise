from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Passenger, Flight, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
# to make function based view as drf import ...
from rest_framework.decorators import api_view

from rest_framework import status

from rest_framework import viewsets
# Create your views here.

# function based.
@api_view(['POST']) # this thing is imp.
def find_flights(request):
    flights = Flight.objects.filter(DepartureCity=request.data['DepartureCity'], ArrivalCity=request.data['ArrivalCity'], DateOfDeparture=request.data['DateOfDeparture'])

    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(FlightNumber=request.data['flightid'])

    passenger = Passenger()
    passenger.Fname = request.data['Fname']
    passenger.Lname = request.data['Lname']
    passenger.Mname = request.data['Mname']
    passenger.Email = request.data['email']
    passenger.Phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.Flight = flight
    reservation.Passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)



class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


