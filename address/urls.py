from django.urls import path
from .views import CreateAddress , DeleteAddress ,UpdateAddress , Get

urlpatterns = [
    path('create/', CreateAddress.as_view() , name ="create_address"),
    path('<int:id_address>/delete/' ,  DeleteAddress.as_view() , name="delete_address"),
    path('<int:id_address>/update/' ,  UpdateAddress.as_view() , name="update_address"),
    path('' ,  Get.as_view() , name="get_address"),

]
