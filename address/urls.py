from django.urls import path
from .views import CreatePatientAddress , CreateDoctorAddress , DeleteAddress ,UpdateDoctorAddress , UpdatePatientAddress ,GetDoctorAddress , GetPatientAddress

urlpatterns = [
    path('patient/create/', CreatePatientAddress.as_view() , name ="create_patient_address"),
    path('doctor/create/', CreateDoctorAddress.as_view() , name ="create_doctor_address"),
    path('<int:address_id>/delete/' ,  DeleteAddress.as_view() , name="delete_address"),
    path('patient/<int:address_id>/update/' ,  UpdatePatientAddress.as_view() , name="update_patient_address"),
    path('doctor/<int:address_id>/update/' ,  UpdateDoctorAddress.as_view() , name="update_doctor_address"),
    path('patient/' ,  GetPatientAddress.as_view() , name="get_patient_address"),
    path('doctor/' ,  GetDoctorAddress.as_view() , name="get_doctor_address"),
    
]
