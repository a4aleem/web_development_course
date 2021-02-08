# cart/urls.py
from django.urls import path
# from .views import hello
# from .views import hello_render

from .views import *
urlpatterns = [
    #path('', get_welcome_data, name='homepage'),
    path('insert', insert_customer, name='insert_customer'),
    path('update', update_customer, name='update_customer'),
    path('get', get_customer, name='get_customer'),
    path('delete', delete_customer, name='delete_customer'),

    path ('getadvanced', get_customer_advanced, name='get_customer_advanced'),
    #path('render_html', hello_render, name="hello_render"),
    #path('square/<int:number>', square, name="square")
]
