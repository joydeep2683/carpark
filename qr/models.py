import uuid
from django.db import models


class QRDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid.uuid4
    )
    car_id = models.ForeignKey(
        'car.Car',
        on_delete=models.CASCADE
    )
    qr_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'qr_qr_detail'


