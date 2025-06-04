from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, CartItem
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


def prod(request, myid):
    product = Product.objects.filter(id=myid)
    param = {'product': product[0]}
    return render(request, 'blog/product.html', param)


def category(request, category):  
    allProd = []
    scatprod = Product.objects.values('sub_category', 'id').filter(category=category)
    cats = {item['sub_category'] for item in scatprod}

    for cat in cats:
        prod = Product.objects.filter(sub_category=cat, category=category)
        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProd.append([prod, range(1, nSlide), nSlide])

    param = {
        'allProd': allProd,
        'category': category
    }
    
    context = {**param, ** params}
    return render(request, 'blog/category.html', context)


def sub_category(request, sub_category):
    products = Product.objects.filter(sub_category=sub_category)
    category = products.first().category if products.exists() else ''
    n = len(products)
    nSlides = ceil(n / 4)
    
    par = {
        'products': products,
        'sub_category': sub_category,
        'category': category,
        'nSlides': nSlides
    }
    
    con = {**params, **par}
    return render(request, 'blog/sub_category.html', con)


def tracker(request):
    return HttpResponse("Tracker")


def search(request):
    return HttpResponse("Search")


def checkout(request):
    return HttpResponse("Checkout")



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'blog/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, item_id):
    product = Product.objects.get(id=item_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')



