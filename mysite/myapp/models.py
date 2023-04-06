from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(null=True, max_length=200)
    price = models.IntegerField(null=True)
    description = models.CharField(null=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name