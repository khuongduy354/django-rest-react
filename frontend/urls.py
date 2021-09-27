from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='frontend'),
    path('join',views.index),
    path('create',views.index),
    path('room/<str:roomCode>',views.index),
]