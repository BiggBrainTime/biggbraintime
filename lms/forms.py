from django import forms
from django.forms import ModelForm
from .models import Profile, Course, Lecture, Tag, Comment, Enrollment, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'username', 'password')#Validators have to be added or not?
        labels = {
            # 'first_name':'First Name',
            # 'last_name':'Last Name',
            # 'email':'Email',
            'username': 'Username',
            'password': 'Password',            
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender','dob','institute','state','phone','display_pic','is_instructor')
        labels = {
            'gender':'Gender',
            'dob':'Date of Birth',
            'institute':'Institute',
            'state':'State',
            'phone':'Phone Number',
            'display_pic':'Profile Picture',
            'is_instructor':'Are you an instructor?'
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class LectForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('lec_num','desc', 'title','link')

