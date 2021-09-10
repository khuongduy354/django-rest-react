from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .serializer import LeadSerializer
from .models import Lead
# Create your views here.
class LeadListView(generics.ListAPIView):
    queryset=Lead.objects.all()
    serializer_class=LeadSerializer