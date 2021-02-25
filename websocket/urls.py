
from django.urls import include, path
from . import views
import gbaragboscrumy


app_name = 'websocket'
urlpatterns = [
    path('test/', views.test,name="test"),
    path('connect/', views.connect, name='connect'),
    path('disconnect/', views.disconnect, name='disconnect'),
    # path('send_message/', views.send_message, name='send_message'),
    # path('recent_messages/', views.recent_messages, name='recent_messages')
   
]