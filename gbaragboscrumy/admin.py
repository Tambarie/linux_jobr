from django.contrib import admin

from . models import GoalStatus, ScrumyGoals,ScrumyHistory
from .forms import *

admin.site.register(GoalStatus)
admin.site.register(ScrumyHistory)
admin.site.register(ScrumyGoals)
# admin.site.register(SignupForm)

# Register your models here.
