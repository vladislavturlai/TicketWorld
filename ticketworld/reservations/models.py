from datetime import datetime

from django.db import models

from ticketworld.reservations.data import SellingOptions, ReservationStatus


class Event(models.Model):
    title = models.CharField(max_length=512)


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(reservations__status__in=Reservation.RESERVATION_ACTIVE_STATUSES)


class UnavailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(reservations__status__in=Reservation.RESERVATION_ACTIVE_STATUSES)


class Ticket(models.Model):
    SELLING_OPTION_CHOICES = (
        (SellingOptions.EVEN, 'Even'),
        (SellingOptions.ALL_TOGETHER, 'All together'),
        (SellingOptions.AVOID_ONE, 'Avoid one')
    )

    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='tickets')
    seat_number = models.IntegerField()
    selling_option = models.CharField(choices=SELLING_OPTION_CHOICES, max_length=64, null=True)

    objects = models.Manager()
    available = AvailableManager()
    unavailable = UnavailableManager()


class Reservation(models.Model):
    RESERVATION_ACTIVE_STATUSES = [ReservationStatus.OPEN, ReservationStatus.PAID, ReservationStatus.PARTIALLY_PAID]
    RESERVATION_STATUS = (
        (ReservationStatus.OPEN, 'Open'),
        (ReservationStatus.PAID, 'Paid'),
        (ReservationStatus.PARTIALLY_PAID, 'Partially paid'),
        (ReservationStatus.FAILED, 'Failed')
    )
    tickets = models.ManyToManyField(Ticket, related_name='reservations')
    date_created = models.DateTimeField(default=datetime.now)
    status = models.CharField(choices=RESERVATION_STATUS, max_length=64, default=ReservationStatus.OPEN)
