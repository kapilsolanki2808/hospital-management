from django.contrib import admin
from .models import DoctorSpecility,Doctor,Patient,Presciption #,Category,Staff
# Register your models here.

# class DoctorAdmin(admin.ModelAdmin):
#   list_display = ['name', 'email', 'contact_number','qualification','specilist']
admin.site.register(Doctor)
admin.site.register(DoctorSpecility)
admin.site.register(Presciption)
# admin.site.register(Category) 

class PatientAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'contact_number','gender','DOB','address','blood_group']
admin.site.register(Patient,PatientAdmin)