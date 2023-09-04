import uuid
from django.db import models

class Trip(models.Model):
    TRIP_TYPE_CHOICES = [
        ('TS', 'Trip Start')
        ('TE', 'Trip End')
    ]
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4
    )
    car_id = models.ForeignKey(
        'car.Car',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField()
    lat = models.FloatField()
    long = models.FloatField()
    type = models.CharField(
        max_length=2, 
        choices=TRIP_TYPE_CHOICES
    )

    class Meta:
        db_table = 'trip_trip'
