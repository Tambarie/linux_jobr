from django import forms
from django.contrib.auth.models import Permission
from django.db.models import fields
from django.db.models.fields import CharField
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name','email', 'password','username']



class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields =['goal_name','user' ]
        Permissions =[
            ('can_create_personal_weekly','Create Personal Weekly')]
        


class MoveGoalForm(forms.ModelForm):
    goal_name = CharField(max_length =150)

    class Meta:
        model = ScrumyGoals
        fields = ['goal_name','goal_status']