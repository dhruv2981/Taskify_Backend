from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
