from django.db import models
from datetime import datetime
from PIL import Image

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mpv = models.BooleanField(default=False)
    birthday_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.first_name

    # def save(self):
    #     super().save()
    #     img = Image.open(self.photo.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)

