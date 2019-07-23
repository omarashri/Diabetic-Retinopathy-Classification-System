from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    address = models.CharField(max_length=25, null=True, blank=True)
    mobile_number = models.CharField(max_length=11, null=True, blank=True)
    last_checked = models.DateField(null=True, blank=True)
    health_condition = models.CharField(max_length=15, null=True, blank=True)


class Image(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(None)
    date = models.DateField(default=datetime.today())
    side = models.CharField(default='L', max_length=1)
    stage = models.CharField(default='1', max_length=10)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})

    def __str__(self):
        return self.image.url
