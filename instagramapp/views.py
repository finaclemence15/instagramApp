from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Image, Profile, Comments
from .forms import NewImageForm,NewProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    profile = Profile.objects.all()
    return render(request, 'index.html', {'images': images}, {'profile': profile})

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
            image.username = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})   
 

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id=current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.bio = current_user
            profile.save()
        return redirect('profile')

    else:
        form = NewProfileForm()
    return render(request, 'profile.html', {"form": form}) 

# @login_required(login_url='/accounts/login/')
# def myaccount(request):
#   current_user = request.user
#   myImage = Image.objects.filter(username=current_user)
#   myProfile = Profile.objects.filter(username = current_user).first()
#   return render(request, 'profile.html', {"myImage":myImage, "myProfile":myProfile})