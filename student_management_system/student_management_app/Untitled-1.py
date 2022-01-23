def loginUser(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return render(request, '/admin_home')
        else: 
            messages.error(request, 'Invalid Login details')
            return render(request, 'login.html')

def getUserDetails(request):
    if request.user!=None:
        return HttpResponse('User: '+request.user.email+ ' usertype : '+request.user.user_type)
    else:
        return HttpResponse('Please Login First')
        return HttpResponseRedirect('/')

