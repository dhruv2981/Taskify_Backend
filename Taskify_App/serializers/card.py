from rest_framework import serializers
from Taskify_App.models import *

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields='__all__'