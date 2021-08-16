from rest_framework import serializers


from ticketworld.reservations.models import Reservation, Ticket
from ticketworld.reservations.services.validation import ReservationValidationService


class ReservationCreateSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), many=True)

    class Meta:
        model = Reservation
        fields = ['tickets', ]

    def validate_tickets(self, tickets):
        # Make sure that that the list is not empty
        if not tickets:
            raise serializers.ValidationError({'msg': 'Ticket numbers must be provided'})

        validation_service = ReservationValidationService(tickets)

        # Make sure that tickets are available
        unavailable_tickets_ids = validation_service.unavailable_tickets_ids()
        if unavailable_tickets_ids:
            raise serializers.ValidationError({'msg': 'The following tickets are unavailable',
                                               'ids': unavailable_tickets_ids})

        # Validate according to selling_options
        errors = validation_service.validate_selling_options()

        if errors:
            raise serializers.ValidationError({'msg': errors})

        return tickets


class TicketReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['event', 'seat_number', 'selling_option']


class ReservationListSerializer(serializers.ModelSerializer):
    tickets = TicketReadSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ['tickets', 'date_created', 'status']
