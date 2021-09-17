from django.db.models import query
from django.shortcuts import render
from .serializer import RoomSerializer
from rest_framework import generics
from .models import Room
from leads import models
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
