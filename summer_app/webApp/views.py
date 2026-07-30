from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 


# Create your views here.


def home(request): 
	return render(request,'home.html',{})

def about(request): 
	return render(request,'about.html',{})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Account created succesfully")
			print("New user was created")
			#return redirect("login")
	else:
		form = UserCreationForm()

	return render(request, "register.html",{"form":form})