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
params = index()

def function(request):
    return render(request, 'blog/home.html', params)

def about(request):
    return render(request, 'blog/about.html', params)

def contact(request):
    return render(request, 'blog/contact.html',params)

def cart(request):
    return render(request, 'blog/cart.html', params)


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

    param = {
        'allProds': allProds,
        'category': category
    }
    return render(request, 'blog/category.html', param)


def sub_category(request, sub_category):
    products = Product.objects.filter(sub_category=sub_category)
    category = products.first().category if products.exists() else ''
    n = len(products)
    nSlides = ceil(n / 4)
    
    param = {
        'products': products,
        'sub_category': sub_category,
        'category': category,
        'nSlides': nSlides
    }
    return render(request, 'blog/sub_category.html', param)


def tracker(request):
    return HttpResponse("Tracker")


def search(request):
    return HttpResponse("Search")


def checkout(request):
    return HttpResponse("Checkout")





