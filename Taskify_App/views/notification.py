from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *

# Create your views here.


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
