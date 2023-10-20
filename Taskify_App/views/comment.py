from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *

# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
