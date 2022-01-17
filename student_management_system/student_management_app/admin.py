# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from student_management_app.models import CustomUser
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)