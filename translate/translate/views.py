from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    
    language = TranslatePage.objects.all()
    
    return render(request , 'home.html', {'language': language,})
    
def translate(request):
    
    malumot = get_object_or_404(TranslatePage)
    
    return render(request, 'malumot.html', {"malumot": malumot})