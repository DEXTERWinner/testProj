from django.db import models

#Making table for "Student"
class Student(models.Model):
	last_name = models.CharField(max_lenght=40)
	first_name = models.CharField(max_lenght=30)
	middle_name = models.CharField(max_lenght=40)
	birthday = models.DateField()
	stud_card = models.CharField(max_lenght=10)
	group = models.ForeignKey(Group)

#Making table for "Group"	
class Group(models.Model):
	name = models.CharField(max_lenght=10)
	warden = models.ForeignKey(Student)