# Generated by Django 4.0.4 on 2022-06-06 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_contactus_delete_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='calibration_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]