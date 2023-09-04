from django.db import models
from qr.models import QRDetail

import uuid

class Users(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid.uuid4
    )
    country_code = models.CharField(max_length=5)
    mobile_number = models.IntegerField()
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_users'


class UserDetails(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        db_index=True, 
        default=uuid.uuid4
    )
    user_id = models.ForeignKey(
        'Users', 
        on_delete=models.CASCADE,   
    )
    name = models.CharField(max_length=150, default=None)
    gender = models.CharField(max_length=1, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_user_details'


class UserPreference(models.Model):
    user_id = models.ForeignKey(
        'Users', 
        on_delete=models.CASCADE
    )
    dnd_on = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_user_preference'


