"""Characters serializers."""


#  Django REST Framework
from rest_framework import serializers

# Models
from backend.models import Character


class CharacterModelSerializer(serializers.ModelSerializer):
    """Character model serializer."""

    class Meta:
        """Meta class."""
        model = Character
        fields = '__all__'
