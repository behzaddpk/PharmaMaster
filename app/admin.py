from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
