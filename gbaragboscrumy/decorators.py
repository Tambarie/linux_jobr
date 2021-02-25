from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *


def unauthorized_user (view_function):
    def wrapper_function (request, *args, **kwargs):
        if User.objects.get(groups__name = 'Admin'):
            return redirect ('gbaragboscrumy:login')

        else:
            return view_function(request,*args, **kwargs)
        return wrapper_function


def allowed_users(allowed_roles =[]):
    def decorator(view_function):
        def wrapper_function(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_function(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not allowed to view this page')
            return wrapper_function
    return decorator


