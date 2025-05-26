from django.db import models
import datetime
from django.core.validators import MinValueValidator
import os

class Product(models.Model):
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    number_of_stock = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=200, default='')
    published_date = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to='blog/images/', default='')
    
    def __str__(self):
        return self.product_name
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)     



