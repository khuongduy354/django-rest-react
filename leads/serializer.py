from django.db import models
from rest_framework import serializers
from .models import Lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields=('id','name','message','email')