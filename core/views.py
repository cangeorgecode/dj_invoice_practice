from django.shortcuts import render
from .models import Customer, Item, Invoice

def index(request):
    context = {
        'invoices': Invoice.objects.all()
    }
    return render(request, 'core/index.html', context)
