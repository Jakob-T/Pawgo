# Generated by Django 4.2 on 2024-02-03 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawgoapp', '0004_alter_topup_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topup',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 10, 20, 28, 355642, tzinfo=datetime.timezone.utc)),
        ),
    ]