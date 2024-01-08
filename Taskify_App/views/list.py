from rest_framework import viewsets
from Taskify_App.serializers import ListSerializer
from Taskify_App.models.list import List
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from Taskify_App.models import Project


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        list_obj = self.get_object()
        project = Project.objects.get(pk=list_obj.project.id)
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to delete list in this project.")
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Adjust this line based on your request data
        project = Project.objects.get(pk=request.data['project'])
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to create list in this project.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        list_obj = self.get_object()
        project = Project.objects.get(pk=list_obj.project.id)
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to update list in this project.")
        return super().update(request, *args, **kwargs)
