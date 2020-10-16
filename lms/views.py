from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Course, User, Lecture, Tag, Comment, Enrollment, Replies
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def videopage(request, course_id, lecnum):
    course = Course.objects.get(course_id  = course_id)
    lectcount = Lecture.objects.filter(course__course_id = course_id).count()
    totallect = Lecture.objects.filter(course__course_id = course_id)
    lects = Lecture.objects.filter(course__course_id = course_id, lec_num = lecnum)
    comments = Comment.objects.filter(lecture__lec_num = lecnum)
    replies = Replies.objects.filter()
    return render(request,'module_display.html',{'course':course, 'lects':lects, 'totallect':totallect,'lectcount':lectcount, 'comments':comments, 'replies':replies})

def course_info(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    lects = Lecture.objects.filter(Course = crse).order_by('lec_num')
    enroll = Enrollment.objects.filter(Course = crse)
    return render(request,'course_info.html',{'crse':crse, 'lects':lects, 'enroll':enroll})


def signin(request):
    if request.method == "POST":
        email_sn = request.POST.get('email_sn','')
        password_sn = request.POST.get('password_sn','')
        update = User.objects.filter(email=email_sn,password=password_sn)
        if len(update)==0:
            return render(request,'login.html',{'error':True})
        else:
            return render(request,'index.html')   #index.html=homepage
    else:
        return render(request,'login.html',{'error':False})


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name_sp','')
        email = request.POST.get('email_sp','')
        password = request.POST.get('password_sp','')
        gender = request.POST.get('gender_sp','N')
        dob = request.POST.get('dob_sp','')
        institute = request.POST.get('institute_sp','')
        state = request.POST.get('state_sp','')
        dp = request.POST.get('dp_sp','')
        instructor = request.POST.get('instructor_sp','')

        if gender!='' and gender not in "MFO":
            gender='N'
        gender = gender[0]

        user = User(name=name, email=email, password=password, gender=gender, dob=dob, institute=institute, state=state, display_pic=dp, is_instructor=instructor)
        user.save()
        return render(request,'index.html')   #index.html=homepage
    else:
        return render(request,'login.html',{'error':False})

def insert_comment(request):
    return