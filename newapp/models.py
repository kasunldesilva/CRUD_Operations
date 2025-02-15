
from django.db import models

# Create your models here.
class Member(models.Model):
    
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    details=models.CharField( max_length=300)