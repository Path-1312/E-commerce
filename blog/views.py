from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, CartItem
from math import ceil


def index():
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    sorted_cats = sorted(cats)
    for cat in sorted_cats:
        prod = Product.objects.filter(category=cat).order_by('product_name')
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    return {'allProds':allProds}
params = index()

def function(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        cart_quantities = {item.product.id: item.quantity for item in cart_items}
    else:
        cart = request.session.get('view_cart', {})
        cart_quantities = {int(k): int(v) for k, v in cart.items()}
    param = {'cart_quantities': cart_quantities,}
    context = {**params, **param}
    return render(request, 'blog/home.html', context)

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
    cart_quantities = {item.product.id: item.quantity for item in cart_items}
    p = {'cart_items': cart_items, 'total_price': total_price, 'cart_quantities': cart_quantities}
    c = {**p, **params}
    return render(request, 'blog/cart.html', c)

def add_to_cart(request, item_id):
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product_id=item_id,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    referer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referer)


def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(user=request.user, product_id=item_id)
    except CartItem.DoesNotExist:
        return redirect('cart:view_cart')

    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    referer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referer)




