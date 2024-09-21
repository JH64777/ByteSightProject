from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from .forms import StegoForm
from .apps import StaganalysisConfig
from Functions.Hash import MakeName
from Functions.ReadyInputData import ReadyXdata

def StegoMainPage(request): # 스테가날리시스 메인 페이지
    variables = {'loggedin' : False}
    return render(request, "staganalysis/StegoMainPage.html", variables)

@csrf_exempt

def SubmitIMG(request): # 이미지 업로드 후 처리
    if request.method == 'POST':
        values = {}
        form = StegoForm(request.POST, request.FILES)
        if form.is_valid():
            stegoimg = form.save(commit=False) # 사진에 대한 정보 가져오는 코드인 것 같음 (잘 모르겠다)
            ext = stegoimg.imgfile.name.split(".")[-1] # 확장자 추출
            stegoimg.imgfile.name = MakeName() + '.' + ext # 파일 이름 변경
            stegoimg.save() # 파일 저장
            
            image_path = stegoimg.imgfile.path # 전체 경로 + 파일 이름/확장자 추출

            Xdata = ReadyXdata(image_path) # 입력 데이터 전처리
            values["percent"] = round(StaganalysisConfig.model.predict(Xdata)[0][0] * 100, 2) # 인공지능 예측 실행
            values["imgpath"] = "/media/" + stegoimg.imgfile.name
            return render(request, "staganalysis/StegoResult.html", values)
    return Http404("오류가 발생했습니다.")