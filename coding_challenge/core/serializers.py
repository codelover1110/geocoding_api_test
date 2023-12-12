import json
from rest_framework import serializers, request
from coding_challenge.core.models import (
    Geocode,
)
from django.contrib.auth.models import User

class GeoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geocode
        fields = "__all__"
