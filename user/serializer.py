from rest_framework import serializers
from user.models import Users

class UserSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField()
    mobile_number = serializers.CharField()
    username = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = ('country_code', 'mobile_number', 'username', )