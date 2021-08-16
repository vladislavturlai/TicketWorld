# Generated by Django 3.2.6 on 2021-08-16 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_alter_ticket_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='reservations.event'),
        ),
    ]
