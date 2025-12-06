from django.shortcuts import render
from .models import About, Contact

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    about_data = About.objects.first()
    return render(request, 'pages/about.html', {'about': about_data})

def contact(request):
    contact_data = Contact.objects.first()
    return render(request, 'pages/contact.html', {'contact': contact_data})
