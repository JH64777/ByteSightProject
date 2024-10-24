from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from .forms import StegoForm
from .apps import StaganalysisConfig
from Functions.Hash import MakeName
from Functions.ReadyInputData import ReadyInputData
from Functions.ExtractFile import Extract
from json import loads
import os

def StegoMainPage(request): # 스테가날리시스 메인 페이지
    variables = {'loggedin' : request.session["loggedin"]}
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

            Xdata = ReadyInputData(image_path) # 입력 데이터 전처리
            values["percent"] = round(StaganalysisConfig.model.predict(Xdata)[0][0] * 100, 2) # 인공지능 예측 실행
            values["imgpath"] = "/media/" + stegoimg.imgfile.name
            return render(request, "staganalysis/StegoResult.html", values)
    return Http404("오류가 발생했습니다.")


@csrf_exempt
def ExtractIMG(request): # 파일 추출 및 다운로드 관련 쿼리문
    data = None
    body = loads(request.body.decode("utf-8"))
    baseDir = os.path.dirname(__file__).replace("\\", "/")
    path = baseDir[:baseDir.rfind("/")] + body["IMGpath"]
    with open(path, 'rb') as f:
        data = f.read()
        f.seek(data.find(b"\xff\xda"))
        f.seek(data.find(b"\xff\xd9") + 2)
        # SOS 아랫 부분에 ff d9라는 데이터는 EOI밖에 없으므로 f.seek()으로 ff da부터 찾은 뒤에 그 뒤에 있을 EOI 시그니처를 찾는 작업을 한 것이다.
        data = f.read() # 숨겨져 있는 데이터 부분을 가져온다.
        extractedFileObject, mimeType, ext = Extract(data) # cursor가 ff d9 위치에 있으므로 그 뒤에 있는 데이터를 가지고 오는 작업
        file = HttpResponse(extractedFileObject, content_type=mimeType) # 전송할 파일 준비
        file['Content-Disposition'] = f'attachment; filename="Extract.{ext}"'
        file['X-File-Extension'] = ext  # 확장자를 커스텀 헤더로 추가
        return file # 응답 데이터


######## AI 모델 새롭게 만들고 테스트해본 결과 (2024-09-29)
# 사진, 파일과 같은 큰 데이터가 숨겨져 있는 경우 잘 감지하는 것으로 확인
# 다만, 글자, 비교적 작은 용량의 파일일 경우(txt파일) 올바르게 감지하지 못하는 것을 확인