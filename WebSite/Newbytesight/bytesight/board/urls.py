from django.urls import path
from . import views

urlpatterns = [
    path("<str:boardCategory>/<int:pageNumber>", views.BoardPage, name="BoardPage"),
    path("<str:boardCategory>/<int:pageNumber>/<str:postID>", views.PostPage, name="PostPage"),
    path("<str:boardCategory>/<int:pageNumber>/<str:postID>/<str:fileName>", views.DownloadFile, name="FileDownload"),
    path("<str:boardCategory>/makepost", views.MakePostPage, name="MakingPost"),
    path("<str:boardCategory>/post/submit", views.SubmitPost, name="submitPost"),
]