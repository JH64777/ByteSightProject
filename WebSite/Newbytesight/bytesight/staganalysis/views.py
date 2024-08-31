from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from .forms import StegoForm
import tensorflow as tf
from Functions.Hash import MakeName
from Functions.ReadyInputData import ReadyXdata

model = tf.keras.models.load_model('C:/Users/asdew32/Desktop/Newbytesight/bytesight/AI_Model/model_17.keras') # 모델 불러오기

def StegoMainPage(request): # 스테가날리시스 메인 페이지
    variables = {'loggedin' : False}
    return render(request, "staganalysis/StegoMainPage.html", variables)

@csrf_exempt

def SubmitIMG(request): # 이미지 업로드 후 처리
    if request.method == 'POST':
        form = StegoForm(request.POST, request.FILES)
        if form.is_valid():
            stegoimg = form.save(commit=False) # 사진에 대한 정보 가져오는 코드인 것 같음 (잘 모르겠다)
            ext = stegoimg.imgfile.name.split(".")[-1] # 확장자 추출
            stegoimg.imgfile.name = MakeName() + '.' + ext # 파일 이름 변경
            stegoimg.save() # 파일 저장
            
            image_path = stegoimg.imgfile.path # 전체 경로 + 파일 이름/확장자 추출

            Xdata = ReadyXdata(image_path) # 입력 데이터 전처리
            accuracy = model.predict(Xdata) # 인공지능 예측 실행
            return HttpResponse(f"정확도 : {accuracy}")
    return Http404("오류가 발생했습니다.")