from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name','email', 'password','username']



class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields =['goal_name','user' ]
