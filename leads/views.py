from django.db.models import query
from django.shortcuts import render
from .serializer import RoomSerializer
from rest_framework import generics
from .models import Room
# Create your views here.

class CreateRoomView(generics.CreateAPIView):
    querset=Room.objects.all()
    serializer_class=RoomSerializer
