from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Car Make')
    description = models.CharField(null=False, max_length=1000)
    country_of_origin = models.CharField(null=True, max_length=100, default='Unknown')
    founded_year = models.IntegerField(
        null=True,
        validators=[MinValueValidator(1886), MaxValueValidator(2024)]
    )

    def __str__(self):
        return self.name


# CarModel model
class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('HATCHBACK', 'Hatchback'),
    ]

    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=True)
    name = models.CharField(null=False, max_length=30, default='Car Model')
    car_type = models.CharField(null=False, max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.DateField(null=True)
    seats = models.IntegerField(null=True, validators=[MinValueValidator(2), MaxValueValidator(8)])

    def __str__(self):
        return self.name
