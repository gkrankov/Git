from django.shortcuts import render
from .models import Couple

def home(request):
    couple = Couple.objects.first()  # Retrieve data from the Couple model
    return render(request, 'home/home.html', {'couple': couple})

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'contact/contact.html')