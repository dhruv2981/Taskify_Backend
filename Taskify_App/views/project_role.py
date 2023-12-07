from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class Project_roleViewSet(viewsets.ModelViewSet):
    queryset = Project_role.objects.all()
    serializer_class = Project_roleSerializer
    permission_classes = [IsAuthenticated]
   
