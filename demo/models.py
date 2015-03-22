from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	rollno=models.IntegerField()
	branch=models.CharField(max_length=10)
	phone_no=models.IntegerField()
	def __str__(self):
		return self.name

class Hobbies(models.Model):
	"""docstring ass Hobbies"""
	hobby_name=models.CharField(max_length=200)
	student =models.ForeignKey(Student)

	def __str__(self):
		return self.hobby_name
	