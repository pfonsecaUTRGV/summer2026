from django.urls import path, include 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
	path('',views.home, name ='home'),
	path('about/',views.about, name ='about'),
	path('register/',views.register, name ='register'),
	path('login/',auth_views.LoginView.as_view(template_name="login.html"), name ='login'),
	path('logout/',auth_views.LogoutView.as_view(), name ='logout'),
	path('about/',views.about,name='about'),
	path('profile/',views.profile,name="profile"),
	path('search/',views.pokemon_search,name = "pokemon_search"),
	path('pokemon/save/',views.save_pokemon,name="save_pokemon"),
	path('pokemon/saved/',views.saved_pokemon,name="saved_pokemon")
]
