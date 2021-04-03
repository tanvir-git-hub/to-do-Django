from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(MyUser, UserAdmin)

UserAdmin.fieldsets += ("Custom fields set", {'fields':('mobile_number',)}),