from rest_framework import serializers
from Taskify_App.models import *

class Project_roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_role
        fields='__all__'