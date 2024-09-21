from django.http import HttpResponseNotFound, HttpResponse
from urllib.parse import quote
import os

# Create your views here.
def DownloadExample(request, ScenarioNum): # 시나리오 파일을 다운로드 시켜주는 함수
    filename = None # 파일 이름
    response = None # 최종 응답 메시지
    filepath = None # 파일 경로
    match ScenarioNum: # 시나리오 번호에 따른 각 파일 경로 지정
        case 1:
            filepath = "C:/Users/asdew32/Desktop/final_project/WebSite/Newbytesight/bytesight/static/scenario/test.zip"
            print(filepath)
        case 2:
            filepath = "C:/Users/asdew32/Desktop/final_project/WebSite/Newbytesight/bytesight/static/scenario/test2.zip"
        case _:
            return HttpResponseNotFound("찾으시는 자료가 없습니다.")

    filename = filepath.split('/')[-1] # 파일 이름만 추출

    with open(filepath, "rb") as f:
        response = HttpResponse(f, content_type="application/zip") # zip파일 형태의 MIME Type

        encodedFilename = quote(filename) # 제목에 한국어 같은거 들어가면 URL에서 사용할 수 있는 형태로 변환
        response['Content-Disposition'] = f"attachment; filename*=utf-8''{encodedFilename}"

    return response