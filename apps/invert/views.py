# Create your views here.
from .models import Inversion
from .serializers import InversionSerializer
from rest_framework import viewsets

class InvertViewSet(viewsets.ModelViewSet):
    serializer_class=InversionSerializer
    queryset=Inversion.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user) 
        serializer.save()
