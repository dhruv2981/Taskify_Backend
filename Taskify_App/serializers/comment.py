from rest_framework import serializers
from Taskify_App.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'