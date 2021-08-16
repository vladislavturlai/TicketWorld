from ticketworld.reservations.models import Ticket


class TicketsData:
    @staticmethod
    def num_available_tickets_after_reservation(reservation_tickets):
        ticket_ids = [ticket.id for ticket in reservation_tickets]

        event_id = reservation_tickets[0].event.id

        available_tickets_num = Ticket.available.filter(event=event_id).exclude(id__in=ticket_ids).count()
        return available_tickets_num

    @staticmethod
    def unavailable_tickets_ids_from_given(tickets):
        ticket_ids = [ticket.id for ticket in tickets]

        return list(Ticket.unavailable.filter(id__in=ticket_ids).values_list('id', flat=True))