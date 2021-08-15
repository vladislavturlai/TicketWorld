from datetime import datetime

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=512)


class Ticket(models.Model):
    TICKET_STATUS_CHOICES = (
        ('RESERVED', 'Reserved'),
        ('TMP_RESERVED', 'Temporarily reserved'),
        ('FREE', 'Free')
    )
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    seat_number = models.CharField(max_length=64)
    status = models.CharField(choices=TICKET_STATUS_CHOICES, max_length=64)


class Reservation(models.Model):
    RESERVATION_STATUS = (
        ('OPEN', 'Open'),
        ('PAID', 'Paid'),
        ('PARTIALLY_PAID', 'Partially paid'),
        ('FAILED', 'Failed')
    )
    tickets = models.ManyToManyField(Ticket, related_name='reservations')
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(choices=RESERVATION_STATUS, max_length=64)


class TicketReservation(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
