from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError


# Model to store train details
class Train(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=50)

    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    total_seats = models.IntegerField()  # Total seats available in the train
 
    def available_seats(self):  
        # Calculate total seats already booked for this train
        booked = self.reservations.aggregate(
            total=Sum('seats_booked')
        )['total'] or 0

        # Return remaining seats
        return self.total_seats - booked
    
    def __str__(self):
        # Display train name and number in admin or shell
        return f"{self.train_name} ({self.train_number})"


# Model to store passenger details
class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        # Display full name of passenger
        return f"{self.first_name} {self.last_name}"


# Model to store reservation details
class Reservation(models.Model):
    # Link reservation to a train
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='reservations')
    
    # Link reservation to a passenger
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    
    seats_booked = models.IntegerField()  # Number of seats booked in this reservation
    created_at = models.DateTimeField(auto_now_add=True)  # Time when booking is created

    def save(self, *args, **kwargs):
        # Check if seats booked is valid (should be greater than 0)
        if self.seats_booked <= 0:
            raise ValidationError("Seats must be greater than 0")

        # Prevent booking more seats than available
        if self.seats_booked > self.train.available_seats():
            raise ValidationError("Not enough seats available")

        # Save the reservation if validation passes
        super().save(*args, **kwargs)
    
    def __str__(self):
        # Display reservation info (Passenger - Train)
        return f"{self.passenger} - {self.train}"