from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/',views.course_info, name = "course_info"),
    path('<int:course_id>/modules'/views.course_modules, name="module")
]