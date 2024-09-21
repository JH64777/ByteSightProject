# 잠시 보류 여기서 파일을 설치하게끔 하는 경로를 만들 것
from django.urls import path
from . import views

urlpatterns = [
    path("<int:ScenarioNum>", views.DownloadExample, name="ScenarioDownloader")
]