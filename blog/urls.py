from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.function, name='bloghome'),
    path('about/', views.about, name='about'),
    path('contact us/', views.contact, name="contact"),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
    path('product/<int:myid>', views.prod, name='Product'),
    path('category/<str:category>', views.category, name="category"),
    path('sub category/<str:sub_category>', views.sub_category, name="sub_category"),
    path('cart/', views.view_cart, name="view_cart"),
    path('add/<int:item_id>', views.add_to_cart, name="add_to_cart"),
    path('remove/<int:item_id>', views.remove_from_cart, name="remove_from_cart"),
]
