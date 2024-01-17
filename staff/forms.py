from django import forms
from . models import Patient,Doctor,Presciption, DoctorSpecility
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # fields = ['first_name','last_name','email','contact_number','doctor','DOB','gender','address','blood_group']
        fields = '__all__'

class SignUPForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = '__all__'
        fields = ['first_name','last_name','email','username','contact_number','image','specilist','password']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Presciption
        fields = '__all__'
    # fields = ['name','email','username','contact_number','image','specilist','password']

class DoctorSpecilityForm(forms.ModelForm):
    class Meta:
        model = DoctorSpecility
        fields = '__all__'

class SearchPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name']