from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CubingSerializer
from .models import Cubing

# Create your views here.
class CubingViewSet(viewsets.ModelViewSet):
    serializer_class=CubingSerializer
    queryset=Cubing.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self,serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong Object Owner')

        serializer.save()
