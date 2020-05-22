"""Users URLs."""

# Django
from django.urls import path

# Views
from usuarios.views import (
    UserLoginAPIView,
    UserSigUpAPIView,
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSigUpAPIView.as_view(), name='login'),
]
