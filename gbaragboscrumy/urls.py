
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.get_grading_parameters)

]
