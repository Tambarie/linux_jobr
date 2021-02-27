from django.contrib.auth.models import Group
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import random

from .models import ScrumyGoals,User,GoalStatus,ScrumyHistory
from .decorators import allowed_users
from .forms import *




# Create your views here.
def index_view(request):
    group = Group.objects.get(name = 'Developer')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            group.user_set.add(user)
            if user.groups.filter(name = 'Developer').exists():
                messages.success(request, f"Your account has been created successfully")

           

    else:
        form = SignupForm()


    return render(request,'gbaragboscrumy/index.html', {'form':form})


@login_required
def move_goal(request, goal_id):
    # context = {
    #     'error':'A record with that goal id does not exist'
    # }
    # try:
    #     obj = ScrumyGoals.objects.get(goal_id = goal_id)
    # except Exception as e:
    #     return render(request,'gbaragboscrumy/exception.html',context)
    # else:
    #     goalname = obj.goal_name
    # return HttpResponse(goalname) 

    user = request.user
    goal= get_object_or_404(ScrumyGoals, goal_id = goal_id)
    if User.objects.filter(username = user, groups__name = 'Developer').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user == request.user:
                if form.is_valid():
                    if GoalStatus.objects.get(
                        status_name = 'Done Goal') != goal.goal_status:
                        form.save()
                        return redirect('gbaragboscrumy:home')
                    else:
                        messages.error(
                            request,
                            "Your group policy doesn't permit this operation"
                        )

            else:
                messages.error(request, 'You cannot move this goal')
        else:
            form = MoveGoalForm(instance=goal)
        return render(request,'gbaragboscrumy/movegoal.html',{'form': form,'post':goal})

    elif User.objects.filter(username = user, groups__name = 'Quality Assurance').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user != request.user:
                if GoalStatus.objects.get(
                    status_name = 'Verify Goal') == goal.goal_status:
                    if form.is_valid():
                        if GoalStatus.objects.get(
                            status_name = 'Daily Goal') != goal.goal_status \
                            and GoalStatus.objects.get(
                                status_name = 'Done Goal') != goal.goal_status:
                                messages.error(request, 'You cannot perform this operation')
                        else:
                            form.save()
                            return redirect('gbaragboscrumy:home')
                else:
                    messages.error(request,'You can only move a verified goal for this user')
            elif goal.user == request.user:
                if form.is_valid():
                    if GoalStatus.objects.get(
                            status_name='Weekly Goal') == goal.goal_status:
                        messages.error(request,
                                        'You cannot perform this operation')
                    else:
                        form.save()
                        return redirect('gbaragboscrumy:home')
            
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'gbaragboscrumy/movegoal.html',{
            'form': form,
            'post':goal
        })

    elif User.objects.filter(username=user, groups__name='Admin').exists():
            if request.method == 'POST':
                form = MoveGoalForm(request.POST, instance=goal)
                if form.is_valid():
                    goal = form.save(commit=False)
                    goal.save()
                    return redirect('gbaragboscrumy:home')
                else:
                    messages.info(request, 'You cannot perform this operation')
            else:
                form = MoveGoalForm(instance=goal)
            return render(request, 'gbaragboscrumy/movegoal.html',
                        {'form': form, 'post': goal})        

    elif User.objects.filter(username=user, groups__name='Owner').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user == request.user:
                if form.is_valid():
                    goal = form.save(commit=False)
                    goal.save()
                    return redirect('gbaragboscrumy:home')
            else:
                messages.info(request, 'You cannot perform this operation')
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'gbaragboscrumy/movegoal.html',
                      {'form': form, 'post': goal})

# #Lab 13
@login_required
def add_goal(request):
    random_number = random.randrange(1000,99999,2)
    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.goal_id = random_number
            instance.created_by = request.user
            instance.moved_by = request.user
            instance.owner = request.user
            instance.goal_status = GoalStatus.objects.get(status_name = 'Weekly Goal') 
            instance.goal_status.save()
            instance.save()
        
    else:
        form =  CreateGoalForm()
    return render(request,'gbaragboscrumy/addgoal.html', {'form':form})


        # if request.method == 'POST':
        #     random_number = random.randint(1000,9999)
        #     form = CreateGoalForm(request.POST) 
        #     if form.is_valid():
        #         loading = form.save(commit= False)
        #         if loading.user == request.user:       
        #             loading.goal_id = random_number
        #             loading.created_by = request.user
        #             loading.moved_by = request.user
        #             loading.owner = request.user
        #             loading.goal_status =GoalStatus(status_name = 'Weekly Goal')
        #             loading.goal_status.save()
        #             loading.save()
        #             return redirect('gbaragboscrumy.home')

        #     else:
        #         messages.info(request,"You cannot create goal for this user")
        # return render(request,'gbaragboscrumy/addgoal.html', {'form':form})

        

   
     



    # user_one = User.objects.get(username ='louis')
    # status= GoalStatus.objects.get(status_name = 'Weekly Goal')
    # rand = random.randint(1000,9999)
    
    
    # add_goal= ScrumyGoals.objects.create(goal_name = 'Keep Learning Django',
    # goal_id= rand,created_by = 'Louis', moved_by ='Louis',
    # owner ='Louis',goal_status = status, user =user_one)
    # add_goal.save()
    # return HttpResponse ('Sucessfully Added')
    

# def home (request):
#     goal = ScrumyGoals.objects.filter(goal_name = 'Keep Learning Django')
#     output = ', '.join([eachgoal.goal_name for eachgoal in goal])
#     return HttpResponse(output)


#Lab13
@login_required
def home(request):
    scrumygoals = ScrumyGoals.objects.all()
    user = User.objects.all()
    context = {
        'users': user,
        'scrumygoals': scrumygoals
    }

    return render(request, 'gbaragboscrumy/home.html',context)








    # users = User.objects.all()
    # weekly_goals = ScrumyGoals.objects.filter(
    #     goal_status = GoalStatus.objects.get(status_name='Weekly Goal')
    # )
    # daily_goals = ScrumyGoals.objects.filter(
    #     goal_status = GoalStatus.objects.get(status_name='Daily Goal')
    # )

    # verify_goals = ScrumyGoals.objects.filter(
    #     goal_status = GoalStatus.objects.get(status_name='Verify Goal')
    # )
    # done_goals = ScrumyGoals.objects.filter(
    #     goal_status = GoalStatus.objects.get(status_name='Done Goal')
    # )
    

    # context = {
        
    #     'weeklygoal':' '.join([each_goal.goal_name for each_goal in weekly_goals]),
    #     'dailygoal':' '.join([each_goal.goal_name for each_goal in daily_goals]),
    #     'verifygoal':' '.join([each_goal.goal_name for each_goal in verify_goals]),
    #     'donegoal':' '.join([each_goal.goal_name for each_goal in done_goals]),
    #     'users':users
    # }


    




   


    
    



