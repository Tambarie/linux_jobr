from .models import ScrumyGoals,User,GoalStatus,ScrumyHistory
from django.shortcuts import render
from django.http import HttpResponse
import random



# Create your views here.
def get_grading_parameters(request):
    return HttpResponse('Learn Django')

def move_goal(request, goal_id):
    context = {
        'error':'A record with that goal id does not exist'
    }
    try:
        obj = ScrumyGoals.objects.get(goal_id = goal_id)
    except Exception as e:
        return render(request,'gbaragboscrumy/exception.html',context)
    else:
        goalname = obj.goal_name
    return HttpResponse(goalname) 


#Lab 13
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
    users = User.objects.all()
    firstuser = users[0]

    goalstatus = GoalStatus.objects.all()
    weeklygoal = goalstatus[0]
    dailygoal = goalstatus[1]
    verifygoal = goalstatus[2]
    donegoal = goalstatus[3]
    
    goals  = firstuser.scrumygoals_set.all()

    context = {
        'firstuser': firstuser,
        'weeklygoal':weeklygoal,
        'dailygoal':dailygoal,
        'verifygoal':verifygoal,
        'donegoal':donegoal,
        'goals':goals,
        'users':users
    }

    return render(request, 'gbaragboscrumy/home.html',context)



   

    
    



