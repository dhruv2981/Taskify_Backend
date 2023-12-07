from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]


