from django.urls import path
from .views import index,cart,chackout,contact,shopdetail,shop,testimonial,xatolik
from . import views


urlpatterns = [
    path('',index, name="index-page"),
    path('cart/',cart, name="cart-page"),
    path('chackout/',chackout, name="chackout-page"),
    path('contact/',contact, name="contact-page"),
    path('shopdetail/',shopdetail, name="shopdetail-page"),
    path('shop/',shop, name="shop-page"),
    path('testimonial/',testimonial, name="testimonial-page"),
    path('xatolik/',xatolik, name="xatolik-page"),

]