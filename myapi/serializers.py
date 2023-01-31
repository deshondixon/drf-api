from rest_framework import serializers
from .models import myapi


class myapiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at")
        model = myapi
