from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.

def welcome(request):
    
    images = Image.images_all
    return render(request, 'index.html',{"images":images})
