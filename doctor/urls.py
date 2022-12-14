from django.urls import path
from .views import RegisterAPI ,LoginAPI ,UserAPI , Get , GetAll , ChangePasswordAPI
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view() , name ="register"),
    path('login/', LoginAPI.as_view() , name ="login"),
    path('logout/',  knox_views.LogoutView.as_view()  , name ="logout"),
    path('change_password/', ChangePasswordAPI.as_view() , name ="Change_Password"),
    path('', UserAPI.as_view() , name ="get_doctor"),
    path('update/', UserAPI.as_view() , name ="update_doctor"),
    path('<int:doctor_id>/', Get.as_view() , name ="get_doctor"),
    path('all/', GetAll.as_view() , name ="get_doctors"),

]

