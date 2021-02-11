from .models import ScrumyGoals,User,GoalStatus,ScrumyHistory
from django.shortcuts import render
from django.http import HttpResponse
import random



# Create your views here.
def get_grading_parameters(request):
    return HttpResponse('Learn Django')

def move_goal(request, goal_id):
    movegoal = ScrumyGoals.objects.get(pk =1)
    goalname = movegoal.goal_name
    return HttpResponse(goalname) 


#Lab 12
def add_goal(request):
    user_one = User.objects.get(username ='louis')
    status= GoalStatus.objects.get(status_name = 'Weekly Goal')
    rand = random.randint(1000,9999)
    
    
    add_goal= ScrumyGoals.objects.create(goal_name = 'Keep Learning Django',
    goal_id= rand,created_by = 'Louis', moved_by ='Louis',
    owner ='Louis',goal_status = status, user =user_one)
    add_goal.save()
    return HttpResponse ('Sucessfully Added')


# def home (request):
#     goal = ScrumyGoals.objects.filter(goal_name = 'Keep Learning Django')
#     output = ', '.join([eachgoal.goal_name for eachgoal in goal])
#     return HttpResponse(output)


#Lab13

def home(request):
    #goal = ScrumyGoals.objects.filter(goal_name = 'Keep Learning Django')
#    output = ', '.join([eachgoal.goal_name for eachgoal in goal])
#    return HttpResponse(output)
    details = ScrumyGoals.objects.get(pk =1)

    

    dictionary = {
      'goal_name': details.goal_name,
      'goal_id': details.goal_id,
      'user': details.user
    }
    
    return render(request, 'gbaragboscrumy/home.html',dictionary)



   

    
    



