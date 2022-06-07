from pyexpat import model
from django.db import models

class Flight(models.Model):
    FlightNumber = models.CharField(max_length=10)
    OperatingAirlines = models.CharField(max_length=20)
    DepartureCity = models.CharField(max_length=20)
    ArrivalCity = models.CharField(max_length=20)
    DateOfDeparture = models.DateField()
    EstTime = models.TimeField()

    def __str__(self):
        return self.FlightNumber + " - " + self.OperatingAirlines


class Passenger(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Mname = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)

    def __str__(self):
        return self.Fname

class Reservation(models.Model):
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    Passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    


