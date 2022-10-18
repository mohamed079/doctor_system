from django.urls import path
from .views import CreateReview , DeleteReview ,UpdateReview , Get

urlpatterns = [
    path('create/', CreateReview.as_view() , name ="create_review"),
    path('<int:id_review>/delete/' ,  DeleteReview.as_view() , name="delete_review"),
    path('<int:id_review>/update/' ,  UpdateReview.as_view() , name="update_review"),
    path('' ,  Get.as_view() , name="get_reviews"),

]
