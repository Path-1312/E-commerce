from django.contrib import admin

# Register your models here.
from .models import Product, CartItem, Profile

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Profile)

