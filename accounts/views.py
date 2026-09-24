from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import UserProfileForm

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form= UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return HttpResponse("user created!")
    context={"form":form}
    return render(request,"registration/register.html",context)

def edit_user_profile(request):
    if request.method =="POST":
        form=UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return redirect("foodspot_app:index")
    else:
        form=UserProfileForm(instance=request.user.profile)
        
    return render(request, "registration/edit_profile.html",{"form":form})