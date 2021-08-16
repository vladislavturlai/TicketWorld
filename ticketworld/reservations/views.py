from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from ticketworld.reservations.models import Reservation
from ticketworld.reservations.serializers import ReservationListSerializer, ReservationCreateSerializer


class ReservationsViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_classes = {
        'create': ReservationCreateSerializer,
        'list': ReservationListSerializer,
    }
    queryset = Reservation.objects.all().prefetch_related('tickets')
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
