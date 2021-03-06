from lms.views import add_course
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('<int:course_id>/',views.course_info, name = "course_info"),
    path('<int:course_id>/<int:lecnum>/postComment/', views.postComment, name="postComment"),
    path('<int:course_id>/<int:lecnum>/',views.videopage, name="videopage"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('logout/',views.logout, name="logout"),
    #path('instructor_page/', views.login_for_instructor, name='instructor_page'),
    path('login_for_instructor/', views.instructor_login, name='login_for_instructor'),
    path('chatbox/', views.chatbox, name='chatbox'),
    path('middle_page/', views.middle_page, name='middle_page'),
    path('add_course/', views.add_course, name='add_course'),
    path('<int:course_id>/addlecture', views.add_lects, name = 'add_lects'),
    path('<int:course_id>/quiz/', views.quiz_view, name='quiz'),
    path('login_page/', views.login_page, name='login_page'),
    path('<int:user_id>/mycourses/', views.user_courses, name='user_courses'),
]