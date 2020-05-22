"""Character views."""

# DRF
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Serializers
from backend.serializers import CharacterModelSerializer
# Models
from .models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    """Character view set."""

    queryset = Character.objects.all()
    serializer_class = CharacterModelSerializer
    permission_classes = (IsAuthenticated,)
