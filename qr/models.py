import uuid
from django.db import models


class QRDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid.uuid4
    )
    user_id = models.ForeignKey(
        'user.Users',
        on_delete=models.CASCADE
    )
    qr_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'qr_qr_detail'

class QRDelivery(models.Model):
    delivery_pincode = models.CharField(max_length=100)
    deliver_address_1 = models.CharField(max_length=255)
    deliver_address_2 = models.CharField(max_length=255)

    class Meta:
        db_table = 'qr_qr_delivery'

