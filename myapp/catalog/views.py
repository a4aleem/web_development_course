from django.shortcuts import render
from .models import Customer
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def insert_customer(request):
    my_customer = Customer()
    my_customer.customer_id = 5
    my_customer.first_name = "Aleem"
    my_customer.last_name = "Siddiqui"
    my_customer.date_of_birth = datetime.now()
    my_customer.is_gold_customer = False
    my_customer.save()
    text = """<h1>Customer Inserted !</h1>"""
    return HttpResponse(text)

def get_customer(request):
    #all_customers = Customer.objects.all()
    my_customer = Customer.objects.get(pk=3)
    #gender_value_from_db = my_customer.gender
    #gender_display_value = my_customer.get_gender_display()
    text = """<h1>Customer Fetched !</h1> """
    return HttpResponse(text)



def update_customer(request):
    my_customer = Customer.objects.get(pk=3)
    my_customer.first_name='someNewName'
    my_customer.save()
    text = """<h1>Customer Updated !</h1>"""
    return HttpResponse(text)

def delete_customer(request):
    my_customer = Customer.objects.get(pk=3)
    my_customer.delete()
    text = """<h1>Customer Deleted !</h1>"""
    return HttpResponse(text)

def get_customer_advanced(request):
    my_customer = Customer.objects.filter(is_gold_customer=True)
    text = ""
    for customer in my_customer:
   	 text += customer.first_name + ", "
    return HttpResponse(text)
