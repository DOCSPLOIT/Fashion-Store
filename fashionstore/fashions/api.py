from rest_framework import viewsets, permissions
from .models import Fashions
from .serializers import FashionSerializer


class FashionViewset(viewsets.ModelViewSet):
    queryset=Fashions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = FashionSerializer

