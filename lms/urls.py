from lms.views import add_course
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('<int:course_id>/',views.course_info, name = "course_info"),
    path('<int:course_id>/<int:lecnum>/',views.videopage, name="videopage"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('logout/',views.logout, name="logout"),
    path('login_for_instructor/', views.instructor_login, name='login_for_instructor'),
    path('chatbox/', views.chatbox, name='chatbox'),
    path('middle_page/', views.middle_page, name='middle_page'),
    path('add_course/', views.add_course, name='add_course'),
    path('<int:course_id>/addlecture', views.add_lects, name = 'add_lects')
]