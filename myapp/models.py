from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.PositiveIntegerField()
	email=models.EmailField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(default="",upload_to="profile_pic/")

	def __str__(self):
		return self.fname+"-"+self.lname


class Contact(models.Model):
	name=models.CharField(max_length=100)
	mobile=models.PositiveIntegerField()
	email=models.EmailField()
	message=models.TextField()

	def __str__(self):
		return self.name