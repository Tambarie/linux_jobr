
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.get_grading_parameters),
    path('', views.move_goal),
    path('', views.home),
    path('', views.add_goal)

]
