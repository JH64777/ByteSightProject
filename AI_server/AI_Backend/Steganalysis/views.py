from django.shortcuts import render
# Create your views here.

def Stegoanalyzer(request): # 여기다가 AI 동작 함수를 두는 것이 좋을 것 같음
    return render(request, "Steganalysis/AI_resultPage.html")
