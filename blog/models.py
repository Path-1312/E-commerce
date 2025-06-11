from django.db import models
import datetime
from django.core.validators import MinValueValidator
import os
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

category_choices = (
    ('Fashion', 'Fashion'),
    ('Accessories', 'Accessories'),
    ('Electronics', 'Electronics'),
    ('Home', 'Home'),
    ('Kitchen', 'Kitchenware'),
    ('Grocery', 'Grocery'),
    ('Beauty', 'Beauty'),
    ('Toys', 'Toys'),
    ('Sports', 'Sports'),
    ('Stationery', 'Stationery'),
    ('Automotive', 'Automotive'),
    ('Pet', 'Pet'),
    ('Other', "Other")
)

class Product(models.Model):
    product_name = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=20, choices = category_choices,default='Other')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    number_of_stock = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=400, default='')
    published_date = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to='blog/images/', default='', help_text='Recommended image size: 230×200 pixels')
    
    def __str__(self):
        return self.product_name
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)     


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    
    
    
    