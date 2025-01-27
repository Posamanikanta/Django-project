from django.db import models

# Create your models here.
class Register1(models.Model):
    mobile=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
