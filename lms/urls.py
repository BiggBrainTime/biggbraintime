from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('<int:course_id>/',views.course_info, name = "course_info"),
    path('postComment', views.postComment, name="postComment"),
    path('<int:course_id>/<int:lecnum>/',views.videopage, name="videopage"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('logout/',views.logout, name="logout"),
    path('instructor_page/', views.login_for_instructor, name='instructor_page'),

]