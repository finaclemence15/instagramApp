from django.shortcuts import render
from .models import Image

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})