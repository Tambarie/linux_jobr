from django.db import models
from django.contrib.auth.models import User




class User(User):
    # username = models.CharField(max_length=20)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    # email = models.EmailField(max_length=20)
    pass



# Create your models here.

class GoalStatus(User):
    status_name = models.CharField(max_length=20)


class ScrumyGoals (models.Model):
   goal_name =models.CharField(max_length=20)
   goal_id = models.IntegerField()
   created_by = models.CharField(max_length=20)
   moved_by =models.CharField(max_length=20)
   owner = models.CharField(max_length=20)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   goal_status = models.ForeignKey(GoalStatus,on_delete=models.PROTECT)




class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)
    moved_from = models.CharField(max_length=20)
    moved_to = models.CharField(max_length=20)
    time_of_action = models.DateTimeField(auto_now_add=True)
    goal = models.ManyToOneRel(ScrumyGoals, on_delete=models.CASCADE)



