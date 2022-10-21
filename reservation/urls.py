from django.urls import path
from .views import CreateReservation , GetPatientReservation , GetDoctorReservation , DeletePatientReservation , ManageDoctorReservation

urlpatterns = [
    path('<int:id_doctor>/<int:id_address>/create/', CreateReservation.as_view() , name ="create_reservation"),
    path('patient/' ,  GetPatientReservation.as_view() , name="patient_reservation"),
    path('doctor/' ,  GetDoctorReservation.as_view() , name="doctor_reservation"),
    path('doctor/<int:id_reservation>/' ,  ManageDoctorReservation.as_view() , name="manage_doctor_reservation"),
    path('<int:id_reservation>/delete/' ,  DeletePatientReservation.as_view() , name="delete_reservation"),

]
