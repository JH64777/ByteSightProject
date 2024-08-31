from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Accounts
from Functions.Hash import Hashing

def LoginPage(request):
    return render(request, "login/LoginPage.html")

@csrf_exempt
def LoginSubmit(request): # 로그인 쿼리 함수
    submitedID = request.POST['st_id'] # 클라이언트로부터 온 id값
    submitedPWD = Hashing(request.POST['st_password']) # 클라이언트로부터 온 pwd값 (sha 256으로 해싱됨)

    try:
        Accounts.objects.get(id=submitedID, pwd=submitedPWD) # 받은 id,pwd를 통해 조회 (성공하면 예외 X, 실패하면 DoesNotExist 예외 발생)
        return HttpResponse("<script>alert('로그인에 성공하셨습니다!'); window.location.href='/'; </script>")
    except Accounts.DoesNotExist:
        return HttpResponse("<script>alert('아이디 혹은 비밀번호가 일치하지 않습니다.'); window.location.href='/login'; </script>")

