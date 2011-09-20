from django.db import models

	
class Student(models.Model):
	last_name = models.CharField(max_length=40)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=40)
	birthday = models.DateField()
	stud_card = models.CharField(max_length=10)
	group = models.ForeignKey('Group')
	
	
class Group(models.Model):
	name = models.CharField(max_length=10)
	warden = models.ForeignKey(Student, related_name='warden')
