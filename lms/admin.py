from django.contrib import admin

# Register your models here.
from . models import User, Course,Lecture,Tag,Comment,Enrollment,Replies

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Enrollment)
admin.site.register(Replies)

# admin.site.register()
# admin.site.register()
