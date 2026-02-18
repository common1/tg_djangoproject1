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
