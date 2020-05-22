"""Backend Angular URLs."""

# Django
from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter
# Views
from backend.views import CharacterViewSet

router = DefaultRouter()
router.register(r'character', CharacterViewSet, basename='character')
urlpatterns = [
    path('', include(router.urls)),
]
