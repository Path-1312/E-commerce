from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, CartItem
from math import ceil


def index(cart_quantities):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    sorted_cats = sorted(cats)
    
    for cat in sorted_cats:
        prod = Product.objects.filter(category=cat).order_by('product_name')

        for product in prod:
            product.adjusted_stock = max(product.number_of_stock - cart_quantities.get(product.id, 0), 0)
        
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    return {'allProds': allProds}

def get_cart_quantities(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        return {item.product.id: item.quantity for item in cart_items}
    else:
        cart = request.session.get('view_cart', {})
        return {int(k): int(v) for k, v in cart.items()}

def get_adjusted_stock(product, cart_quantities):
    quantity_in_cart = cart_quantities.get(product.id, 0)
    return max(product.number_of_stock - quantity_in_cart, 0)

def function(request):
    cart_quantities = get_cart_quantities(request)
    params = index(cart_quantities)
    
    context = {**params, 'cart_quantities': cart_quantities}
    return render(request, 'blog/home.html', context)


def about(request):
    cart_quantities = get_cart_quantities(request)
    params = index(cart_quantities)
    return render(request, 'blog/about.html', params)

def contact(request):
    cart_quantities = get_cart_quantities(request)
    params = index(cart_quantities)
    return render(request, 'blog/contact.html',params)


def prod(request, myid):
    product = get_object_or_404(Product, id=myid)
    cart_quantities = get_cart_quantities(request)
    params = index(cart_quantities)
    quantity_in_cart = cart_quantities.get(product.id, 0)
    product.number_of_stock -= quantity_in_cart
    
    param = {'product': product, 'cart_quantities': cart_quantities}
    context = {**params, **param}
    return render(request, 'blog/product.html', context)


def category(request, category):  
    allProd = []
    scatprod = Product.objects.values('sub_category', 'id').filter(category=category)
    cats = {item['sub_category'] for item in scatprod}
    sorted_cats = sorted(cats)

    for cat in sorted_cats:
        prod = Product.objects.filter(sub_category=cat, category=category).order_by('product_name')
        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProd.append([prod, range(1, nSlide), nSlide])
        cart_quantities = get_cart_quantities(request)
        for product in prod:
            product.adjusted_stock = max(product.number_of_stock - cart_quantities.get(product.id, 0), 0)
    params = index(cart_quantities)
    param = {
        'allProd': allProd, 'category': category, 'cart_quantities': cart_quantities
        }
    
    context = {**param, ** params}
    return render(request, 'blog/category.html', context)


def sub_category(request, sub_category):
    products = Product.objects.filter(sub_category=sub_category)
    category = products.first().category if products.exists() else ''
    n = len(products)
    nSlides = ceil(n / 4)
    
    cart_quantities = get_cart_quantities(request)
    params = index(cart_quantities)
    par = {
        'products': products,
        'sub_category': sub_category,
        'category': category,
        'nSlides': nSlides,
        'cart_quantities': cart_quantities
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
    cart_quantity = get_cart_quantities(request)
    params = index(cart_quantity)
    for item in cart_items:
        item.product.adjusted_stock = max(item.product.number_of_stock - cart_quantities.get(item.product.id, 0), 0)
        
    p = {'cart_items': cart_items, 'total_price': total_price, 'cart_quantities': cart_quantities}
    c = {**p, **params}
    c.update(params)
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
    cart_item = CartItem.objects.get(user=request.user, product_id=item_id)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    referer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referer)

def delete_from_cart(request, item_id):
    cart_item = CartItem.objects.get(user=request.user, product_id=item_id)
    cart_item.delete()
    referer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referer)























# def category(request, category):  
#     allProd = []
#     scatprod = Product.objects.values('sub_category', 'id').filter(category=category)
#     cats = {item['sub_category'] for item in scatprod}

#     cart_quantities = get_cart_quantities(request)

#     for cat in cats:
#         prod = Product.objects.filter(sub_category=cat, category=category)
        
#         # Add adjusted_stock here too:
#         for product in prod:
#             product.adjusted_stock = max(product.number_of_stock - cart_quantities.get(product.id, 0), 0)
        
#         n = len(prod)
#         nSlide = n // 4 + ceil((n / 4) - (n // 4))
#         allProd.append([prod, range(1, nSlide), nSlide])
        
#     param = {
#         'allProd': allProd, 'category': category, 'cart_quantities': cart_quantities
#         }
    
#     context = {**param, **params}
#     return render(request, 'blog/category.html', context)
