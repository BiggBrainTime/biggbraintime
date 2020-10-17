from django.http import request
from lms.forms import CourseForm, LectForm, UserForm
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
    comment = Comment.objects.filter(lecture__lec_num = lecnum, parent=None)
    replies = Comment.objects.filter(lecture__lec_num = lecnum).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.sno not in replyDict.key():
            replyDict[reply.sno]= [reply]
        else:
            replyDict[reply.sno].append(reply)
    #replies = Replies.objects.filter()
    return render(request,'module_display.html',{'course':course, 'user':request.user,'lects':lects, 'totallect':totallect,'lectcount':lectcount, 'comment':comment})

def postComment(request,course_id, lecnum):
        if request.method=="POST":
            comment = request.POST.get("comment")
            user =request.user
            lectureLecnum = request.POST.get("lectureLecnum")
            lecture = Lecture.objects.get("sno=lectureLecnum ")
            parentsno = request.POST.get("sno=parentsno ")
            if parentsno == "":
                comment = Comment(comment=comment, user=user, lecture=lecture)
                comment.save()
                message.success(request, "your reply posted successfully")

            else:
                parent=Comment.objects.get(sno=parentsno)

                comment = Comment(comment=comment, user=user, lecture=lecture)
                comment.save()
                message.success(request, "your comment posted successfully")

        return redirect(f"127.0.0.1:8000/{course_id}/{lecnum}")


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


#def insert_comment(request):
    #return


def add_course(request):
    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return redirect('add_lects', course_id = form.instance.course_id)

    else:
        print("Error Form Invalid!")

    return render(request, 'add_course.html', {'form':form})


def chatbox(request):
    return render(request, 'chatbox.html')

def instructor_login(request):
    return render(request, 'login_for_instructor.html')

def middle_page(request):
    return render(request, 'middle_page.html')

def add_lects(request, course_id):
    if(request.method=="POST"):
        form1 = LectForm(request.POST)
        if form1.is_valid():
            lec_num = request.POST.get('lec_num')
            desc = request.POST.get('desc')
            title = request.POST.get('title')
            link = request.POST.get('link')
            crse = Course.objects.get(course_id = course_id)
            if crse is not None:
                Lecture.objects.create(lec_num = lec_num,name = title, desc = desc, title = title, link = link, course = crse)
                messages.success(request, '* Lecture Added')
        else:
            messages.info(request,'* Wrong Input')
        return redirect('add_lects', course_id = course_id)
    
    form1 = LectForm()
    crse = Course.objects.get(course_id = course_id)
    return render(request, 'add_lecture.html',{'form1':form1, 'crse':crse})


def quiz_view(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    return render(request, 'quiz.html', {'crse': crse})

def login_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)

    else:
        print("Error Form Invalid!")

    return render(request, 'login_new.html', {'form':form})
