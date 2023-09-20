import uuid
from django.db import models

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
    chasis_id = models.CharField(max_length=100, default=None)
    engine_id = models.CharField(max_length=100, default=None)

    class Meta:
        db_table = 'car_car'

    def __str__(self) -> str:
        return super().__str__()
