from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.

def welcome(request):

    images = Image.images_all
    return render(request, 'index.html',{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_image(search_cagegory) # Image.search_by_category(search_cagegory)
        message = f"{search_category}"
        return render(request, 'search.html',{"message":message,"images": searched_category})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
