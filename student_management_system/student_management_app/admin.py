from django.contrib import admin
from .models import Students, Staffs, Courses
# Register your models here.

admin.site.register(Students)
admin.site.register(Staffs)
admin.site.register(Courses)