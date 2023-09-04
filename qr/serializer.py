from rest_framework import serializers

class QRDetailSerializer(serializers.ModelSerializer):
    qr_link = serializers.CharField(required=False)
    