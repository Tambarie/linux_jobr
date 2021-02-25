from django.contrib import admin


from django.contrib import admin
from .models import  ConnectionModel, ChatMessage

# Register your models here.
admin.site.register(ConnectionModel)
admin.site.register(ChatMessage)
