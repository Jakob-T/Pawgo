from django.db import models
from random import randint
from django.utils import timezone
from datetime import timedelta
from djmoney.models.fields import MoneyField


def generate_code():
    return ''.join(str(randint(0, 9)) for _ in range(12))

class TopUp(models.Model):
    code=models.CharField(max_length=12, default=generate_code, blank=True)
    value=MoneyField(max_digits=10, decimal_places=2, default_currency='EUR', default=0)
    expiration_date=models.DateTimeField(default=timezone.now()+timedelta(days=10))
    isused=models.BooleanField(default=False)

    def mark_as_expired(self):
        if not self.isused and timezone.now() > self.expiration_date:
            self.isused = True
            self.save()

