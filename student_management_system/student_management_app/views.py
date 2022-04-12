from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def pageNotFound(request):
    return render(request, 'error_templates/404/404_template.html')

def forbiddenPage(request):
    pass