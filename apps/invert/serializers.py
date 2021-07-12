from rest_framework import serializers
from .models import Inversion

class InversionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inversion
        read_only_fields=(
            "created_by",
            "created_at",
        ),
        fields=(
            "idea",
            "id",
            "reversed_idea",
            "wrong",
         
        )