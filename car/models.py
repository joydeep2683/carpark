import uuid
from django.db import models
from user.models import Users

class Car(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid.uuid4
    )
    user_id = models.ForeignKey(
        'user.Users', 
        on_delete=models.CASCADE
    )
    car_number = models.CharField(max_length=50, default=None)
    start_lat = models.FloatField()
    start_lon = models.FloatField()
    finish_lat = models.FloatField()
    finish_lon = models.FloatField()

    class Meta:
        db_table = 'car_car'
