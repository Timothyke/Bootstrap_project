from django.shortcuts import render
from .models import Card

def index(request):
    cards = Card.objects.all()
    return render(request, 'main/index.html', {'cards': cards})
