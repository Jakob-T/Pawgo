# Generated by Django 5.0.1 on 2024-02-02 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disputes', '0002_rename_text_dispute_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispute',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 4, 20, 24, 588132, tzinfo=datetime.timezone.utc)),
        ),
    ]
