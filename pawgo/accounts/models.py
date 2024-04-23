from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from pawgoapp.models import TopUp

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    is_walker=models.BooleanField(default=False)
    token_balance=MoneyField(max_digits=10, decimal_places=2, default_currency='EUR', default=0)
    used_topups=models.ManyToManyField(TopUp, blank=True)

    

    def __str__(self):
        return self.username


class Review(models.Model):
    job = models.ForeignKey('jobs.Job', on_delete = models.CASCADE, null = True)
    text = models.CharField(max_length = 512, blank = True)
    date = models.DateTimeField(auto_now_add = True)
    rating = models.DecimalField(default = 0.0, max_digits = 3, decimal_places = 2)

    def __str__(self):
        return f"At {self.date}, By {self.reviewer}, Rating:{self.rating}, Additional comments: {self.text}"