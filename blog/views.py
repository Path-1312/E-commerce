from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def function(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'blog/home.html', params)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def cart(request):
    return render(request, 'blog/cart.html')

def prod(request, myid):
    product = Product.objects.filter(id=myid)
    param = {'product': product[0]}
    return render(request, 'blog/product.html', param)









def tracker(request):
    return render(request, 'blog/contact.html')
def search(request):
    return render(request, 'blog/contact.html')
def checkout(request):
    return render(request, 'blog/contact.html')




