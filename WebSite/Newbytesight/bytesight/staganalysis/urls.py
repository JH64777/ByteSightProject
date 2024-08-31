from django.urls import path
from . import views

urlpatterns = [
    path("", views.StegoMainPage, name="StegoMainPage"),
    path("SubmitImage", views.SubmitIMG, name="IMGsubmit"),
]