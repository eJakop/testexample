from .models import Guide
from rest_framework import viewsets, permissions
from .serializers import GuideSerizlizer


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GuideSerizlizer
