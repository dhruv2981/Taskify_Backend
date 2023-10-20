from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
