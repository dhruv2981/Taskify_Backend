from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
