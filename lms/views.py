from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Course, User, Lecture, Tag, Comment, Enrollment
# Create your views here.

def videopage(request, course_id, lecnum):
    course = Course.objects.get(course_id  = course_id)
    lectcount = Lecture.objects.filter(Course = course).count()
    totallect = Lecture.objects.filter(Course = course)
    lects = Lecture.objects.filter(Course = course, lec_num = lecnum)
    chats = []
    return render(request,'module_display.html',{'course':course, 'lects':lects, 'totallect':totallect,'lectcount':lectcount})

def course_info(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    lects = Lecture.objects.filter(Course = crse).order_by('lec_num')
    enroll = Enrollment.objects.filter(Course = crse)
    return render(request,'course_info.html',{'crse':crse, 'lects':lects, 'enroll':enroll})

def course_modules(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    lects = Lecture.objects.filter(Course = crse).order_by('lec_num')
    return render(request,'module_display.html',{'crse':crse, 'lects':lects})
