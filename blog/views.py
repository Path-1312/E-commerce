from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math


def function(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + math.ceil((n/4) - (n//4))
    
    params = {'product': products, 'number_of_slides': nSlides, 'range': range(1, nSlides)}
    return render(request, 'blog/home.html', params)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def cart(request):
    return render(request, 'blog/cart.html')

def prod(request):
    products = Product.objects.all()
    param = {'product': products}
    return render(request, 'blog/product.html', param)









def tracker(request):
    return render(request, 'blog/contact.html')
def search(request):
    return render(request, 'blog/contact.html')
def checkout(request):
    return render(request, 'blog/contact.html')




