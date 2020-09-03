from django.db import models
from django.contrib.auth.models import User


class Fashions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_main = models.ImageField(upload_to='media/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='media/%Y/%m/%d/')
    image_2 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    owner = models.ForeignKey(User,
                              related_name="fashions",
                              on_delete=models.CASCADE, null=True)
