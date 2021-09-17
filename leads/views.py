from django.http import response
from .serializer import CreateRoomSerializer, RoomSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, generateCode
from leads import models

from leads import serializer
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer


class CreateRoomView(APIView):
    serializer_class=CreateRoomSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializor=self.serializer_class(data=request.data)
        if serializor.is_valid():
            guest_can_pause=serializor.data.get('guest_can_pause')
            votes_to_skip=serializor.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset: 
               room=queryset[0]
               room.guest_can_pause=guest_can_pause 
               room.votes_to_skip=votes_to_skip
               room.save(update_fields=['guest_can_pause','votes_to_skip'])
               return Response(RoomSerializer(room).data,status=status.HTTP_200_OK)
            else:
                room=Room.objects.create(guest_can_pause=guest_can_pause,votes_to_skip=votes_to_skip,host=host)
                return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED)
        return Response({'Bad Request':'Invalid data'},status=status.HTTP_400_BAD_REQUEST)