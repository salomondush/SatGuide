from django.db import models

from django.contrib.auth.models import AbstractUser

from datetime import date
# Create your models here.

# ##Add more information on these models
# class User(AbstractUser):
#     phone = models.CharField(max_length=20)
#     date_of_birth = models.DateField()
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100, blank=True)
#     is_doctor = models.BooleanField()
#     gender = models.CharField(max_length=1, blank=True)

#     def is_valid_user(self):
#         return ((len(self.username) > 0) and (len(self.gender) > 0)
#                 and (len(self.email) > 0) and (self.date_of_birth 
#                 > date(1818, 1, 1)))

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#         #You can also use hasattr to avoid the need for exception catching:
#         #hasattr.(u, "doctor"), which returns "True" or "False"

class School(models.Model):
    name = models.CharField(max_length=200)
    acceptance_rate = models.FloatField()
    average_percentage_class = models.FloatField()
    average_percentage_ne = models.FloatField()
    sat_averge = models.FloatField()
    phy_subj_average = models.FloatField()
    math_subj_average = models.FloatField()
    bio_subj_average = models.FloatField()
    chem_subj_average = models.FloatField()
    toelf_average = models.FloatField()

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")
    sat = models.IntegerField()
    phy_subj = models.IntegerField()
    math_subj = models.IntegerField()
    bio_subj = models.IntegerField()
    chem_subj = models.IntegerField()
    toelf = models.IntegerField()
    report_percentage = models.FloatField()
    national_exams = models.IntegerField()

"""Adding migrations to apps Now, run python manage.py migrate --fake-initial , 
   and Django will detect that you have an initial migration and that the tables 
   it wants to create already exist, and will mark the migration as already applied.
"""