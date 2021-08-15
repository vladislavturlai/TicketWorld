# Generated by Django 3.2.6 on 2021-08-15 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('PAID', 'Paid'), ('PARTIALLY_PAID', 'Partially paid'), ('FAILED', 'Failed')], max_length=64)),
                ('tickets', models.ManyToManyField(related_name='reservations', to='reservations.Ticket')),
            ],
        ),
    ]
