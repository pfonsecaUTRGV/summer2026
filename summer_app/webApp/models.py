from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


#Creating the profile table for each registered users
class Profile (models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="profile",
		)
	phone_number = models.CharField(
		max_length= 10,
		blank=True,
		)
	campus = models.CharField(
		max_length = 20,
		blank = True,
		)
	bio = models.TextField(
		max_length = 200,
		blank = True,)

	def __str__(self):
		return f"{self.user.username}'s profile"

