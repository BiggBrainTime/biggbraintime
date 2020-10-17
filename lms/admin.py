from django.contrib import admin

# Register your models here.
from . models import  Course,Lecture,Tag,Comment,Enrollment,Replies,Profile, Chatroom,Chat

admin.site.register(Profile)
#admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Enrollment)
admin.site.register(Replies)
admin.site.register(Chatroom)
admin.site.register(Chat)
