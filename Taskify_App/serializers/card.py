from rest_framework import serializers
from Taskify_App.models import *
from .comment import CommentSerializer

class CardSerializer(serializers.ModelSerializer):
    comments =CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Card
        fields='__all__'