from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Course, User, Lecture, Tag, Comment, Enrollment
# Create your views here.

def course_info(request, course_id):
    crse = Course.objects.get(course_id  = course_id)
    lects = Lecture.objects.filter(course = crse).order_by('lec_num')
    enroll = Enrollment.objects.filter(course = crse) 
    return render(request,'course_info.html',{'crse':crse, 'lects':lects, 'enroll':enroll})
