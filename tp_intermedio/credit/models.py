from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Credit(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=40)
    amount = models.IntegerField()
    
   
    
    def __str__(self):
        return f"{self.code} {self.description} | amount: {self.amount}"