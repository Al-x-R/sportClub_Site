from django.db import models
from datetime import datetime

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mpv = models.BooleanField(default=False)
    birthday_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name