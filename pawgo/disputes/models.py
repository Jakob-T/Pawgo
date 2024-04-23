from django.db import models
from accounts.models import CustomUser
from django.utils import timezone



class Dispute(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dispute_post')
    walker=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dispute_blame')
    pub_date = models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=512)
    ishandled=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}: {self.user}"
    
    
