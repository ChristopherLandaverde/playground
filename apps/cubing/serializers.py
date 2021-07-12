from rest_framework import serializers

from .models import Cubing


class CubingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cubing
        read_only_fields = (
            "created_by",
            "created_at"
        )
        fields = (
            "id",
            "described_idea",
            "compared_idea",
            "associate_idea",
            "analyzed_idea",
            "argued_idea",
            "applyed_idea"
         
           
        )