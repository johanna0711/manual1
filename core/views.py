from django.shortcuts import render

# Create your views here.


def home(request, plantilla="home.html"):
    return render(request, plantilla)

def index(request, plantilla="index.html"):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def portfolio(request, plantilla="portfolio.html"):
    return render(request, plantilla)
# Create your views here.
