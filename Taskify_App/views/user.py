from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


