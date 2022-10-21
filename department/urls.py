from django.urls import path 
from .views import GetAll , Get , CreateDepartment , DeleteDepartment , UpdateDepartment

urlpatterns = [
    path('' ,  GetAll.as_view() , name="get_departments"),
    path('<int:department_id>/' ,  Get.as_view() , name="get_department"),
    path('create/' ,  CreateDepartment.as_view() , name="create_department"),
    path('<int:department_id>/delete/' ,  DeleteDepartment.as_view() , name="delete_department"),
    path('<int:department_id>/update/' ,  UpdateDepartment.as_view() , name="update_department"),

] 
