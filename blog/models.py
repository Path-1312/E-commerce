from django.db import models
import datetime
from django.core.validators import MinValueValidator

class Product(models.Model):
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    number_of_stock = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=200, default='')
    published_date = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to='blog/images/', default='')
    
    def __str__(self):
        return self.product_name



