from django.urls import path
from .views import RegisterAPI ,LoginAPI ,UserAPI , GetAll , ChangePasswordAPI
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view() , name ="register"),
    path('login/', LoginAPI.as_view() , name ="login"),
    path('logout/',  knox_views.LogoutView.as_view()  , name ="logout"),
    path('change_password/', ChangePasswordAPI.as_view() , name ="Change_Password"),
    path('', UserAPI.as_view() , name ="get_patient"),
    path('all/', GetAll.as_view() , name ="get_patients"),

]

