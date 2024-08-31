from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseServerError
from .models import Accounts
from django.views.decorators.csrf import csrf_exempt
import json
from Functions.Hash import Hashing

def SignupPage(request):
    return render(request, "account/AccountPage.html") # 여기다가 html경로 적을 것

@csrf_exempt # django 고유의 CSRF공격을 막기위한 정책 때문에 해당 데코레이터를 작성해 줘야함 (해당 요청에서는 정책을 사용하지 않겠다는 뜻)

def CheckID(request): # 회원가입 시 동일한 아이디/닉네임이 있는지 여부를 검사하는 함수
    reqData = json.loads(request.body.decode("utf-8")) # json데이터를 dictionary 형태로 변환

    if reqData["flag"] == 'ID': # 아이디 검사
        try:
            Accounts.objects.get(id=reqData["contents"]) # Account테이블에서 사용자로부터 요청 받은 id와 동일한 것이 있는지 조회하는 코드
        except Accounts.DoesNotExist: # 존재하지 않다면
            return JsonResponse({"msg" : "사용 가능한 아이디 입니다.", "flag" : True})
        
        return JsonResponse({"msg" : "이미 존재하는 아이디 입니다", "flag" : False}) # json 형태의 응답
    else: # 닉네임 검사
        try:
            Accounts.objects.get(nickname=reqData["contents"]) # Account테이블에서 사용자로부터 요청 받은 닉네임과 동일한 것이 있는지 조회하는 코드
        except Accounts.DoesNotExist: # 존재하지 않다면
            return JsonResponse({"msg" : "사용 가능한 닉네임 입니다.", "flag" : True})
        
        return JsonResponse({"msg" : "이미 존재하는 닉네임 입니다", "flag" : False}) # json 형태의 응답

@csrf_exempt
def AddAccount(request): # 회원 추가 함수
    accountsTable = Accounts() # Insert하기 위해 테이블 객체 생성

    # 각 컬럼에 요청된 값 Insert
    try:
        accountsTable.id = request.POST["st_id"] 
        accountsTable.pwd = Hashing(request.POST["st_password"]) # 비밀번호 해시 폼으로 변경해서 저장
        accountsTable.nickname = request.POST["st_nickname"]
        accountsTable.email = request.POST["st_mail"]
        accountsTable.save() # Insert한 값 DB에 반영
        return HttpResponseRedirect("/") # 홈페이지로 리다이렉션
    except Exception as e:
        print(e)
        return HttpResponseServerError() # 실패시 서버에러 반환
