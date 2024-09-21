from django.shortcuts import render

def HomePage(request):
    variable = None
    if "loggedin" not in request.session: # 만약 세션이 없다면
        request.session["loggedin"] = False
    variable = { "loggedin" : request.session["loggedin"] }
    
    return render(request, "home/HomePage.html", variable)