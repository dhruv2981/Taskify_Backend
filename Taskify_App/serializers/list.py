from rest_framework import serializers
from Taskify_App.models import *
from .card import CardSerializer

class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True,read_only=True)
    class Meta:
        
        model=List
        fields='__all__'