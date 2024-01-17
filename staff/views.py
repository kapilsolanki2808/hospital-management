from django.shortcuts import render,redirect,HttpResponse
from .models import Patient,Doctor,Presciption
from django.contrib.auth.hashers import make_password
from . forms import PatientForm,SignUPForm,PrescriptionForm,DoctorSpecilityForm,SearchPatientForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from datetime import date
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
# import random
# random_number = random.randint(1000,9999)
# print(random_number)




def patient_signup(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_number=request.POST.get('contact_number')
        doctor_id = request.POST.get('doctor')
        doctor = Doctor.objects.get(pk=doctor_id)
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        Appointment_time=request.POST.get('Appointment_time')
        message=request.POST.get('message')
        p = Patient.objects.create(name=name, email= email,
                    contact_number=contact_number,doctor=doctor,DOB=DOB,gender=gender,
                    address=address,blood_group=blood_group,Appointment_time=Appointment_time,
                    message=message)
        p.save()
        return redirect('PatientTable')
    else:
        # form = PatientForm()
        data = Doctor.objects.all()
        return render(request, 'index.html', {'data': data})

def re_appointment(request,id):
    data = Patient.objects.get(id=id)
    new = Patient()
    if request.method =='POST':
        form = PatientForm(request.POST,instance=new)
        if form.is_valid():
            form.save()  
            return render(request,'search.html')     
    else:
        form = PatientForm(instance=data)
        return render(request, 're_appointment.html', {'form':form,'data': data})


class PatientTable(ListView):
    model = Patient
    template_name = 'patients.html'

def check(request):
    data = Doctor.objects.all()
    return render(request,'index.html',{'data':data})


def search_patient(request): 
    # breakpoint()
    if request.method == 'POST':
        form = SearchPatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            data = Patient.objects.filter(name__icontains=name)
            obj = Patient.objects.filter(name__iexact=name)
            for i in obj:
                data1 = Presciption.objects.filter(patient_name=i)
                return render(request, 'search.html', {'data': data, 'form': form,'data1':data1})
            
    else:
        form = SearchPatientForm()
       
        # return render(request,'prescription_list.html',{'data':data1})
    return render(request, 'index.html', {'form': form})

@login_required(login_url='/login/')
def prescription_list(request):
    if request.method == 'GET':
        data1 = Presciption.objects.all()
        return render(request,'prescription_list.html',{'data':data1})


@login_required(login_url='/login/')
def prescription(request):
    user = request.user
    if request.method == 'POST':  
        form = PrescriptionForm(request.POST,request.FILES)
        form.doctor_name = user
        if form.is_valid():
            form.save()
            return redirect("doctor_retrive")
    else:   
        form = PrescriptionForm()
        form.doctor_name = user
    return render(request,'register.html',{'form':form,'form.doctor_name':form.doctor_name})

def experiment(request):
   return render(request,'base.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doctor_retrive') 
        else:
            return render(request, 'sign_in.html')
    else:
        return render(request, 'sign_in.html')


@login_required(login_url='/log_in/')
def doctor_retrive(request):
    a = request.user
    if request.method == 'GET':
        # object_list = [i.first_name for i in Patient.objects.filter(doctor__username = a)]
        object_list = Patient.objects.filter(Appointment_time__gte= date.today(),doctor__username = str(a))
        for i in object_list:
            return render(request, 'doctor_patient.html',{'object_list':object_list})
    return render(request, 'doctor_patient.html')

def add_doctor_specilist(request):
    if request.method == 'POST':
        form = DoctorSpecilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_doctor')
    else:
       form = DoctorSpecilityForm()
    return render(request, 'register.html',{'form':form})


@staff_member_required
def signup_doctor(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(request.POST.get('password'))
            user.save()
            return redirect(check)
    else:
        form = SignUPForm()
    return render(request, 'register.html',{'form':form})


    

@login_required
def logout_view(request):
    logout(request)
    return redirect(doctor_retrive)

def approve_appointment(request,id):
    if request.method == 'GET':
        identity = Patient.objects.get(id=id)
        to_email = identity.email
        a = identity.doctor
        name = identity.name
        subject = request.POST.get("subject", "subject")
        message = request.POST.get("message", f'Hello {name} your appointment has been fixed with Dr. {a}' ) 
        from_email = request.POST.get("from_email", "kapilsolanki.coder@gmail.com")
        to = [str(to_email)]
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, to)
                return redirect('doctor_retrive')
            except BadHeaderError:
                print("Invalid")
                return redirect('doctor_retrive')
        else:
            return HttpResponse("Make sure all fields are entered and valid in email like subject,message,from_email .")
    else:
        return redirect('doctor_retrive')
#############################################################################################################################################################


























# def otp_code_email(request):
#     if request.method == "POST":
#       form = Confirmation(request.POST)
#       if form.is_valid():
#         entered_otp = form.cleaned_data.get('otp_code')
#         if form.is_valid:
#           print("form valid")
#           if entered_otp == random_number:
#             return redirect("save_user")
#           else:
#               return HttpResponse("Invalid OTP")
#     else:
#         form = Confirmation()
#         return render(request, 'otp_code_email.html', {'form': form})
#     return render(request, 'otp_code_email.html', {'form': form})


# class RegisterPatient(View):

#   def get(self, request, *args, **kwargs):
#     self.form = PatientForm()
#     return render(request,"register.html",{'form':self.form})
  
#   def post(self, request, *args, **kwargs):
#     self.form = PatientForm(request.POST)
#     if self.form.is_valid():

#       self.user = self.form.save(commit=False)
#       to_email = self.user.email
#       subject = request.POST.get("subject", "subject")
#       message = request.POST.get("message", str(random_number))
#       from_email = request.POST.get("from_email", "kapilsolanki.coder@gmail.com")
#       to = [str(to_email)]
#       if subject and message and from_email:
#         try:
#           send_mail(subject, message, from_email, to)
#           return redirect('otp_code_email')
#         except BadHeaderError:
#             print("Invalid")
#       else:
#           return HttpResponse("Make sure all fields are entered and valid in email like subject,message,from_email .")
#     else:
#       return render(request,"register.html",{'form':self.form})


