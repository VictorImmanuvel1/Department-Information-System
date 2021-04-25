from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import student,sem1,sem2,sem3,sem4,sem5,event,Profile,Education,oe,ap,article,seminar

class registerform(ModelForm):
    class Meta:
        model=student
        fields='__all__'


class sem1form(ModelForm):
    class Meta:
        model= sem1
        exclude = ('sid',)
        #fields='__all__'

class sem2form(ModelForm):
    class Meta:
        model= sem2
        exclude = ('sid',)
        #fields='__all__'

class sem3form(ModelForm):
    class Meta:
        model= sem3
        exclude = ('sid',)
        #fields='__all__'

class sem4form(ModelForm):
    class Meta:
        model= sem4
        exclude = ('sid',)
        #fields='__all__'

class sem5form(ModelForm):
    class Meta:
        model= sem5
        exclude = ('sid',)
        #fields='__all__'

class eventform(ModelForm):
    class Meta:
        model=event
        fields='__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email', 'designation', 'department', 'doj', 'spint', 'spinre', 'reint']


class EducationUpdateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['d1', 's1', 'c1', 'y1', 'd2', 's2', 'c2', 'y2', 'd3', 's3', 'c3', 'y3', 'd4', 's4', 'c4', 'y4', 'd5',
                  's5', 'c5', 'y5', 'd6', 's6', 'c6', 'y6', 'd7', 's7', 'c7', 'y7', 'd8', 's8', 'c8', 'y8']

class oeForm(forms.ModelForm):
    class Meta:
        model=oe
        exclude=('user',)

class apForm(forms.ModelForm):
    class Meta:
        model=ap
        exclude=('user',)

class articleForm(forms.ModelForm):
    class Meta:
        model=article
        exclude=('user',)

class seminarForm(forms.ModelForm):
    class Meta:
        model=seminar
        exclude=('user',)
