from rest_framework import serializers
from .models import Brainstorm

class BrainstormSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Brainstorm
        read_only_fields = (
            "created_by",
        )
        fields = (
            "id",
            "goals",
            "agenda",
            "outcomes",
            "decisions",
            
        )