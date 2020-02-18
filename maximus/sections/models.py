from django.db import models
from trainers.models import Trainer

# Create your models here.
class Section(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    number_of_lessons = models.IntegerField()
    price = models.FloatField()
    price_unlimited = models.FloatField()

    photo_main_trainings = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main_training = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title