from .models import ScrumyGoals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_grading_parameters(request):
    return HttpResponse('Learn Django')

def move_goal(request, goal_id):
    movegoal = ScrumyGoals.objects.get(pk =1)
    goalname = movegoal.goal_name
    return HttpResponse(f"{goalname}%s" % goal_id) 
