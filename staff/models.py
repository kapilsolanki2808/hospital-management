from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Common(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=180,unique=True,null=True,blank=True)
  contact_number = models.IntegerField(unique=True)
  qualification = models.CharField(max_length=120)

# class Category(models.Model):
#   staff_list = models.CharField(max_length=150,unique=True)
#   def __str__(self):
#     return self.staff_list

class DoctorSpecility(models.Model):
  specility = models.CharField(max_length=150,unique=True)
  def __str__(self):
    return str(self.specility)
  
# class Staff(Common):
#   category = models.ForeignKey(Category, on_delete=models.CASCADE)
#   specilist = models.ForeignKey(DoctorSpecility, on_delete=models.CASCADE)
#   def __str__(self):
#     return str(self.category)
                                
class Doctor(User):
  specilist = models.ForeignKey(DoctorSpecility, on_delete=models.CASCADE)
  contact_number = models.IntegerField()
  image = models.ImageField(upload_to='images',null=True, blank=True)
  def __str__(self):
    return str(self.username)
  
class Patient(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=150)
  contact_number = models.IntegerField()
  doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
  DOB = models.DateField()
  choice = (('male','male'),('female','female'),('other','other'))
  gender = models.CharField(max_length=10,choices = choice)
  address = models.CharField(max_length=200)
  choice = (('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'))
  blood_group = models.CharField(max_length=10,choices = choice)
  Appointment_time = models.DateTimeField()
  message = models.TextField(null=True, blank=True)
  def __str__(self):
    return str(self.name)

# class Appointment(models.Model):
#   start_time = models.DateTimeField()
#   end_time = models.DateTimeField()

class Presciption(models.Model):
  patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
  doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  prescription = models.FileField(upload_to='prescription',null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return str(self.patient_name)