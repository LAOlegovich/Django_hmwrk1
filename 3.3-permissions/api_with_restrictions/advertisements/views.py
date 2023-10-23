from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly

from .filters import AdvertisementFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter

from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated()]
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update","destroy"]:
            return [IsOwnerOrReadOnly(), IsAuthenticated()]
        return []

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        creator = self.request.query_params.get("creator", None)

        if creator is not None:
            queryset = queryset.filter(creator_id  = creator)

        return queryset