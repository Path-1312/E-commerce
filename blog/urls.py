from django.urls import path
from . import views

urlpatterns = [
    path('', views.function, name='bloghome'),
    path('about/', views.about, name='about'),
    path('contact us/', views.contact, name="contact"),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
    path('product/<int:myid>', views.prod, name='Product'),
    path('cart/', views.cart, name="cart"),
    path('category/<str:category>', views.category, name="category"),
    path('sub category/<str:sub_category>', views.sub_category, name="sub_category"),
]
