from django.http import HttpResponseRedirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                elif modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                elif modulename == "student_management_app.StudentViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                elif modulename == "accounts.views":
                    pass 
                else:
                    return HttpResponseRedirect('/admin-home')
            # Staff Page Restriction
            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                elif modulename == "accounts.views":
                    pass 
                else:
                    return redirect('forbidden-page')
            # Student Page Restriction
            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                elif modulename == "accounts.views":
                    pass    
                else:
                    return redirect('forbidden-page')
        else:
            if (request.path == '/login' or modulename == 'django.contrib.auth.urls'):
                pass
            else:
                pass

