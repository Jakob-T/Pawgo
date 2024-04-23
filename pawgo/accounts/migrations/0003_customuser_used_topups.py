# Generated by Django 4.2 on 2024-02-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawgoapp', '0004_alter_topup_expiration_date'),
        ('accounts', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='used_topups',
            field=models.ManyToManyField(blank=True, to='pawgoapp.topup'),
        ),
    ]
