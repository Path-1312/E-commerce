from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index():
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    return {'allProds':allProds}

def function(request):
    params = index()
    return render(request, 'blog/home.html', params)

def basic(request):
    params = index()
    return render(request, 'blog/basic.html', params)


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



def category(request, category):  
    allProds = []
    scatprods = Product.objects.values('sub_category', 'id').filter(category=category)
    cats = {item['sub_category'] for item in scatprods}

    for cat in cats:
        prod = Product.objects.filter(sub_category=cat, category=category)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {
        'allProds': allProds,
        'category': category
    }
    return render(request, 'blog/category.html', params)









def tracker(request):
    return render(request, 'blog/contact.html')
def search(request):
    return render(request, 'blog/contact.html')
def checkout(request):
    return render(request, 'blog/contact.html')




