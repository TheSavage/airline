# Generated by Django 5.1.1 on 2024-11-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_delete_mytest_alter_flight_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]
