from django.shortcuts import render
from trainApp.models import Train, Passenger, Reservation
from trainApp.serializers import TrainSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


# API to find trains based on source, destination and date
@api_view(['POST'])
def find_trains(request):
    # Filter trains based on user input
    trains = Train.objects.filter(
        source=request.data['source'],
        destination=request.data['destination'],
        departure_date=request.data['departure_date']
    )

    # Convert queryset to JSON response
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data)


# ViewSet for Train (provides CRUD operations automatically)
class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()  # Get all train records
    serializer_class = TrainSerializer  # Use TrainSerializer


# ViewSet for Passenger (CRUD operations)
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()  # Get all passengers
    serializer_class = PassengerSerializer


# ViewSet for Reservation (CRUD operations + validation handled in serializer)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()  # Get all reservations
    serializer_class = ReservationSerializer