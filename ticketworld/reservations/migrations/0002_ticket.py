# Generated by Django 3.2.6 on 2021-08-15 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('RESERVED', 'Reserved'), ('TMP_RESERVED', 'Temporarily reserved'), ('FREE', 'Free')], max_length=64)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.event')),
            ],
        ),
    ]
