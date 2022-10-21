from django.urls import path
from .views import CreatePatientAddress , CreateDoctorAddress , DeleteAddress ,UpdateDoctorAddress , UpdatePatientAddress , GetDoctorAddress , GetPatientAddress

urlpatterns = [
    path('patient/create/', CreatePatientAddress.as_view() , name ="create_patient_address"),
    path('doctor/create/', CreateDoctorAddress.as_view() , name ="create_doctor_address"),
    path('<int:id_address>/delete/' ,  DeleteAddress.as_view() , name="delete_address"),
    path('patient/<int:id_address>/update/' ,  UpdatePatientAddress.as_view() , name="update_patient_address"),
    path('doctor/<int:id_address>/update/' ,  UpdateDoctorAddress.as_view() , name="update_doctor_address"),
    path('patient/' ,  GetPatientAddress.as_view() , name="get_patient_address"),
    path('doctor/' ,  GetDoctorAddress.as_view() , name="get_doctor_address"),
    
]
