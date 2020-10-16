from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('<int:course_id>/',views.course_info, name = "course_info"),
    path('<int:course_id>/<int:lecnum>/',views.videopage, name="videopage"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),

]