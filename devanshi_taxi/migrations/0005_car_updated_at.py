# Generated by Django 4.1.13 on 2024-08-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devanshi_taxi', '0004_booking_drop'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]