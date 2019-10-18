from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Image
from .forms import NewImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
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
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})    