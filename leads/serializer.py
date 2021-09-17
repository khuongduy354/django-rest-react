from django.db import models
from rest_framework import serializers
from .models import Room
class RoomSerializer(serializers.Serializer):
    class Meta:
        model=Room
        fields=('code','host','guest_can_pause','votes_to_skip')