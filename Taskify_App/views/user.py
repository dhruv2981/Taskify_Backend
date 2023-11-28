from rest_framework import viewsets
from Taskify_App.serializers import *
from Taskify_App.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    


