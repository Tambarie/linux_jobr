from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL




class User(AbstractUser):
    pass



# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return self.status_name


class ScrumyGoals (models.Model):
    goal_name =models.CharField(max_length=20)
    goal_id = models.IntegerField(SET_NULL)
    created_by = models.CharField(max_length=20)
    moved_by =models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_status = models.ForeignKey(GoalStatus,on_delete=models.CASCADE)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)
    moved_from = models.CharField(max_length=20)
    moved_to = models.CharField(max_length=20)
    time_of_action = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by




