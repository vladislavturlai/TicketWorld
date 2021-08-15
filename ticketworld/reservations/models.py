from datetime import datetime

from django.db import models

from ticketworld.reservations.data import SellingOptions, ReservationStatus


class Event(models.Model):
    title = models.CharField(max_length=512)


class Ticket(models.Model):
    TICKET_STATUS_CHOICES = (
        ('RESERVED', 'Reserved'),
        ('TMP_RESERVED', 'Temporarily reserved'),
        ('FREE', 'Free')
    )
    SELLING_OPTION_CHOICES = (
        (SellingOptions.EVEN, 'Even'),
        (SellingOptions.ALL_TOGETHER, 'All together'),
        (SellingOptions.AVOID_ONE, 'Avoid one')
    )

    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    seat_number = models.CharField(max_length=64)
    status = models.CharField(choices=TICKET_STATUS_CHOICES, max_length=64)
    selling_option = models.CharField(choices=SELLING_OPTION_CHOICES, max_length=64, null=True)


class Reservation(models.Model):
    RESERVATION_STATUS = (
        (ReservationStatus.OPEN, 'Open'),
        (ReservationStatus.PAID, 'Paid'),
        (ReservationStatus.PARTIALLY_PAID, 'Partially paid'),
        (ReservationStatus.FAILED, 'Failed')
    )
    tickets = models.ManyToManyField(Ticket, related_name='reservations')
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(choices=RESERVATION_STATUS, max_length=64, default=ReservationStatus.OPEN)
