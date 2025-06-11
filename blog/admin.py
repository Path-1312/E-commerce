from django.contrib import admin
from .constants import categories
from django import forms
import json
# Register your models here.
from .models import Product, CartItem, Profile, categories

class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('blog/js/dynamic_subcategories.js',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['sub_category'].widget.attrs['data-categories'] = str(categories).replace("'", '"')
        return form
    
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Profile)

