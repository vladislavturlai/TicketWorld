# Generated by Django 3.2.6 on 2021-08-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20210815_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='status',
        ),
    ]