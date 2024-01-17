from django.urls import path
from staff.views import PatientTable,prescription_list, patient_signup,log_in,add_doctor_specilist, check,prescription,experiment,re_appointment, signup_doctor,doctor_retrive,logout_view,approve_appointment,search_patient
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path('patient_signup/',patient_signup, name='patient_signup'),
                path('log_in/',log_in,name='log_in'),
                path('add_doctor_specilist/',add_doctor_specilist,name='add_doctor_specilist'),
                path('signup_doctor/',signup_doctor,name='signup_doctor'),
                path('re_appointment/<int:id>/',re_appointment,name='re_appointment'),
                path('doctor_retrive/',doctor_retrive,name='doctor_retrive'),
                path('prescription_list/',prescription_list,name='prescription_list'),
                path('logout_view/',logout_view),
                path('',check,name='home'),
                path('search_patient/',search_patient,name='search_patient'),
                path('prescription/',prescription,name='prescription'),
                path('experiment/',experiment,name='experiment'),
                path('approve_appointment/<int:id>/',approve_appointment,name='approve_appointment'),
                path('PatientTable/',PatientTable.as_view(),name='PatientTable'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)