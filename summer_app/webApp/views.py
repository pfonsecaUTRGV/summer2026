from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


#Import to update profile 
from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.

#Method for rendering home page
def home(request): 
	return render(request,'home.html',{})

#Method for rendering about page
@login_required
def about(request): 
	return render(request,'about.html',{})

#Method for register a new user
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Account created succesfully")
			print("New user was created")
			return redirect("login")
	else:
		form = UserCreationForm()

	return render(request, "register.html",{"form":form})


	#Method for C-RUD (Read, Update and Delete) the user profile
@login_required
def profile(request):
    profile_object, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            instance=profile_object,
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Your profile was updated successfully.",
            )

            return redirect("profile")

    else:
        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=profile_object
        )

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(
        request,
        "profile.html",
        context,
    )