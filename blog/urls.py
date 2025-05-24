from django.urls import path
from . import views

urlpatterns = [
    path('', views.function, name='bloghome'),
    path('about/', views.about, name='about'),
    path('contact us/', views.contact, name="contact"),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
    path('product/', views.prod, name='Product')
]
