from django.shortcuts import render
from django.http import Http404, HttpResponse
from .forms import SteganographyForm
from django.views.decorators.csrf import csrf_exempt
from Functions.MakeStegoIMG import AppendTail

# Create your views here.
def SteganographyMain(request): # 스테가노그래피 생성 메인 페이지
    variables = {'loggedin' : request.session["loggedin"]}
    return render(request, "steganography/steganographyMain.html", variables)

@csrf_exempt
def SteganographySubmit(request): # 스테가노그래피 생성 요청을 받는 메서드 (커버 이미지, 숨길 파일이 들어옴)
    if request.method == 'POST':
        form = SteganographyForm(request.POST, request.FILES)
        if form.is_valid():
            cover_image = request.FILES.get('coverimg') # 커버 이미지에 대한 데이터를 가져온다
            secret_file = request.FILES.get('secretdata') # 숨기는 파일에 대한 데이터를 가져온다.
            cover_image_binary = cover_image.read() # 커버 이미지에 대한 바이너리 값을 가져온다
            secret_file_binary = secret_file.read() # 숨기는 파일에 대한 바이너리 값을 가져온다.

            stegoImageObject, mimeType = AppendTail(cover_image_binary, secret_file_binary) # 스테가노그래피 사진을 만들고 그 사진의 데이터와 MIME Type을 반환한다
        
            file = HttpResponse(stegoImageObject, content_type=mimeType) # 전송할 파일 준비
            file['Content-Disposition'] = f'attachment; filename="Steganography.jpg"'
            file['X-File-Extension'] = "jpg"  # 확장자를 커스텀 헤더로 추가
            return file # 응답 데이터
    else:
        return Http404("오류가 발생했습니다.")