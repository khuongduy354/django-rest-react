from django.contrib import admin
from django.urls import path
from .views import CreateRoomView,RoomView, getRoom,JoinRoom
urlpatterns = [
    path('room',RoomView.as_view()),
    path('create',CreateRoomView.as_view()),
    path('get-room',getRoom.as_view()),
    path('join-room',JoinRoom.as_view()),
]
