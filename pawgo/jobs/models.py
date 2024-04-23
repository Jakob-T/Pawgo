# Create your models here.
from django.db import models
from accounts.models import CustomUser
from djmoney.models.fields import MoneyField

class Job(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posted_jobs')
    title=models.CharField(max_length=128, unique=True)
    description=models.CharField(max_length=512)
    dog_breed=models.CharField(max_length=128)
    location=models.CharField(max_length=128)
    budget=MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    pub_date = models.DateTimeField()
    duration=models.IntegerField(default=0)
    accepted=models.BooleanField(default=False)
    walked_by=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='walked_jobs')
    U_TIJEKU = 'U tijeku'
    IZVRSEN = 'Izvršen'  
    STATE_CHOICES = [
        (U_TIJEKU, 'U tijeku'),
        (IZVRSEN, 'Izvršen'),
    ]
    
    state=models.CharField(max_length=20, choices=STATE_CHOICES, default=U_TIJEKU)
       
    def __str__(self):
        return f"{self.id}: {self.title}"
