from api import views
from django.urls import path

urlpatterns = [
    path('<int:key>/',views.student_detail,name="student"),
    path('list/',views.student_list,name ="student_list")
]
