from rest_framework import serializers
from trainApp.models import Train, Passenger, Reservation
import re


# Serializer for Train model
class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

    def validate_train_number(self, train_number):
        # Check if train number contains only letters and numbers
        if re.match("^[a-zA-Z0-9]+$", train_number) is None:
            raise serializers.ValidationError(
                "Invalid Train Number. Must be alphanumeric"
            )
        return train_number
    
    def validate(self, data):
        # General validation (currently no extra checks)
        return data


# Serializer for Passenger model
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


# Serializer for Reservation model
class ReservationSerializer(serializers.ModelSerializer):
    # This field shows available seats in the response
    available_seats = serializers.SerializerMethodField()
    
    class Meta:
        model = Reservation
        fields = '__all__'

    def get_available_seats(self, obj):
        # Get available seats from related Train model
        return obj.train.available_seats()

    def validate(self, data):
        train = data['train']
        seats = data['seats_booked']

        # Ensure seats booked is greater than 0
        if seats <= 0:
            raise serializers.ValidationError(
                "Seats must be greater than 0"
            )
        
        # Get current available seats
        available = train.available_seats()

        # Prevent booking more seats than available
        if seats > available:
            raise serializers.ValidationError({
                "error": "Not enough seats available",
                "available_seats": available
            })

        return data