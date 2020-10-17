from django.http import request
from lms.forms import CourseForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Course, Lecture, Tag, Comment, Enrollment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def videopage(request, course_id, lecnum):
    course = Course.objects.get(course_id  = course_id)
    lectcount = Lecture.objects.filter(course__course_id = course_id).count()
    totallect = Lecture.objects.filter(course__course_id = course_id)
    lects = Lecture.objects.filter(course__course_id = course_id, lec_num = lecnum)
    comments = Comment.objects.filter(lecture__lec_num = lecnum)
    #replies = Replies.objects.filter()
    return render(request,'module_display.html',{'course':course, 'lects':lects, 'totallect':totallect,'lectcount':lectcount, 'comments':comments})

def course_info(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    lects = Lecture.objects.filter(course = crse).order_by('lec_num')
    enroll = Enrollment.objects.filter(course = crse) 
    return render(request,'course_info.html',{'crse':crse, 'lects':lects, 'enroll':enroll})


def signin(request):
    if request.method == "POST":
        email_sn = request.POST.get('email_sn','')
        password_sn = request.POST.get('password_sn','')
        
        user = authenticate(email=email_sn,password=password_sn)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful!")
            return redirect("index")
        
        else:
            messages.error(request,"Login Failed!")
            return redirect("index")


        # update = User.objects.filter(email=email_sn,password=password_sn)
        # if len(update)==0:
        #     return render(request,'login.html',{'error':True})
        # else:
        #     return render(request,'index.html')   #index.html=homepage
    else:
        return render(request,'login.html',{'error':False})


def signup(request):
    if request.method == "POST":
        name = request.POST.get('firstname','')
        name = request.POST.get('lastname','')
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
        else:
            gender = gender[0]


        user = User.objects.create_user(name=name, email=email, password=password, gender=gender, dob=dob, institute=institute, state=state, display_pic=dp, is_instructor=instructor)
        user.save()
        messages.success(request,"Your account has been successfully created! Happy learning")
        return redirect("index")   #index.html=homepage
    else:
        return render(request,'login.html',{'error':False})

def logout(request):
    logout(request)
    messages.success("Logged Out Succesfully!")
    return redirect("index")


def insert_comment(request):
    return


def add_course(request):
    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)

    else:
        print("Error Form Invalid!")

    return render(request, 'add_course.html', {'form':form})


def chatbox(request):
    return render(request, 'chatbox.html')

def instructor_login(request):
    return render(request, 'login_for_instructor.html')

def middle_page(request):
    return render(request, 'middle_page.html')

def quiz_view(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    return render(request, 'quiz.html', {'crse': crse})