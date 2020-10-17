from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1, null=True)
    dob = models.DateField(null = True)
    institute = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    display_pic = models.ImageField(upload_to="", default='')  #edit this
    is_instructor = models.BooleanField(default = False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Course(models.Model):
    '''
    for the course and its instructor
    '''
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=5000, null=True)
    course_id = models.AutoField(primary_key = True)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models. DateTimeField(auto_now_add=True)
    last_update = models. DateTimeField(auto_now=True)
    enroll = models.IntegerField(default=0)             #keeping this here coz even if a user deletes his account this still should be visible
    price  = models.IntegerField()

class Lecture(models.Model):
    '''
    for each lecture in the course
    '''
    lec_num = models.IntegerField()
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=3500, null=True)
    title = models.CharField(max_length = 200)
    link = models.URLField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("course", "lec_num"),)
    


class Tag (models.Model):
    '''
    for each tag in a lecture
    '''
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)


class Comment(models.Model):
    '''
    for the comments in the lecture
    '''
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    reported = models.IntegerField(default=0)  #to delete if it reaches some treshold
    deleted = models.BooleanField(default = False)


class Enrollment(models.Model):
    '''
    to keep a track of number of enrollments & to keep a record of rating/reviews of a given course
    '''
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    learner = models.ForeignKey(User,on_delete=models.CASCADE)
    star = models.IntegerField(null=True)
    review = models.TextField(max_length=3500, null=True)
    class Meta:
        unique_together = (("course", "learner"),)
    
class Replies(models.Model):
    replies = models.TextField(max_length=3500)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default  = 0)
    

class Chatroom(models.Model):
    '''
    for the chatroom
    '''
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    learner = models.ForeignKey(User,on_delete=models.CASCADE)
    

class Chat(models.Model):
    ''' 
    for the chats in the chatroom
    '''
    room = models.ForeignKey(Chatroom,on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default = False)
    chat = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    