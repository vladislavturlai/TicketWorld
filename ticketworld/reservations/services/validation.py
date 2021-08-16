from ticketworld.reservations.data import SellingOptions
from ticketworld.reservations.services.data import TicketsData


def _validate_all_together(tickets):
    valid = True
    seat_numbers = [ticket.seat_number for ticket in tickets]

    sorted_seat_numbers = list(sorted(seat_numbers))

    current_seat = sorted_seat_numbers[0]
    for seat in sorted_seat_numbers:
        valid = valid and current_seat == seat
        current_seat += 1

    return valid


def _validate_avoid_one(tickets):
    available_tickets_num = TicketsData.num_available_tickets_after_reservation(tickets)
    valid = available_tickets_num != 1

    return valid


def _validate_even(tickets):
    valid = True

    if len(tickets) % 2 != 0:
        valid = False

    return valid

class ReservationValidationService:
    SELLING_OPTIONS_VALIDATORS = {
        SellingOptions.EVEN: {
            'func': _validate_even,
            'error_message': 'Number of tickets must be even',
        },
        SellingOptions.AVOID_ONE: {
            'func': _validate_avoid_one,
            'error_message': 'Leaving one available ticket is not allowed',
        },
        SellingOptions.ALL_TOGETHER: {
            'func': _validate_all_together,
            'error_message': 'There must be no gaps between seats',
        }
    }

    def __init__(self, tickets):
        self.tickets = tickets

    def unavailable_tickets_ids(self):
        unavailable_seats_ids = TicketsData.unavailable_tickets_ids_from_given(self.tickets)

        return unavailable_seats_ids

    def validate_selling_options(self):
        error_messages = []

        selling_options = set((ticket.selling_option for ticket in self.tickets))

        for selling_option in selling_options:
            validator = self.SELLING_OPTIONS_VALIDATORS.get(selling_option)

            if validator is not None:
                validator_func = validator['func']
                validator_error = validator['error_message']
                result = validator_func(self.tickets)
                if not result:
                    error_messages.append(validator_error)

        return error_messages
