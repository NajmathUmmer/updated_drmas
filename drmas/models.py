from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
	age = models.IntegerField(default=23)
	sex= models.CharField(max_length=10, default='Female')
	
	def __str__(self):
				 return str(self.email)


class Disease(models.Model):
	did=models.IntegerField()
	diagnose=models.CharField(max_length=50)
	description = models.URLField(max_length=128,default='')
	def __str__(self):
				 return str(self.diagnose)

class Symptom(models.Model):
	syd=models.IntegerField()
	symptoms=models.CharField(max_length=50)
	sex=models.CharField(max_length=10,default='')

	def __str__(self):
				 return str(self.symptoms)
	