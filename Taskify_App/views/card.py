from rest_framework import viewsets
from Taskify_App.serializers import CardSerializer
from Taskify_App.models import Card, List, Project
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        card = self.get_object()
        list_obj = List.objects.get(pk=card.list.id)
        project = Project.objects.get(pk=list_obj.project.id)
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to delete card in this project.")
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Adjust this line based on your request data
        list_obj = List.objects.get(pk=request.data['list'])
        project = Project.objects.get(pk=list_obj.project.id)
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to create card in this project.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        card = self.get_object()
        list_obj = List.objects.get(pk=card.list.id)
        project = Project.objects.get(pk=list_obj.project.id)
        if (request.user.role == 'n') and not project.member.filter(id=request.user.id).exists():
            return HttpResponse("You don't have permission to update card in this project.")
        return super().update(request, *args, **kwargs)
