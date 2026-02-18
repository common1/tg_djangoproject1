from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer

def company(request):
    template = 'company/company.html'

    return render(request, template)

def customers(request):
    customers = Customer.objects.all()
    template = 'company/customers.html'
    context = {'customers': customers}

    return render(request, template, context)

def customernew(request):
    data = Customer()
    
    data.first_name = "John"
    data.last_name = "Doe"
    data.email = "john.doe@usn.com"
    data.phone = "333333"
    data.address = "Norway"
    
    data.save()
    
    message = "<h1>New Customer</h1><p>New Customer created successfully</p>"
    
    return HttpResponse(message)
