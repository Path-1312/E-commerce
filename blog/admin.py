from django.contrib import admin
from .constants import categories
from django import forms
import json
# Register your models here.
from .models import Product, CartItem, Profile, categories

     
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    class Media:
        js = ('admin/js/subcategory.js',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['sub_category'].widget = forms.Select()
        form.base_fields['sub_category'].choices = [('', 'Select a sub-category')]
        return form

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['categories_json'] = json.dumps(categories)
        return super().changelist_view(request, extra_context=extra_context)
    
admin.site.register(CartItem)
admin.site.register(Profile)

