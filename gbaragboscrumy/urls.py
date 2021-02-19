
from django.urls import include, path
from . import views
import gbaragboscrumy


app_name = 'gbaragboscrumy'
urlpatterns = [
    path('', views.index_view,name="index_view"),
    path('movegoal/<int:goal_id>', views.move_goal, name = "move_goal"),
    path('addgoal/', views.add_goal,name = "add_goal"),
    path('home/', views.home, name  ="home"),
    path('accounts/',include('django.contrib.auth.urls'),name = "accounts")


    
    # path('', views.home_detail_view),

]