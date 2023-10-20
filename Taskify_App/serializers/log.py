from rest_framework import serializers
from Taskify_App.models import *

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields='__all__'