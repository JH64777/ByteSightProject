from django.shortcuts import render

def HomePage(request):
    variables = {'loggedin': False, 'nickname' : 'Unknown'}
    return render(request, "home/HomePage.html", variables)