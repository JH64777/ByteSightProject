from django.urls import path
from . import views

urlpatterns = [
    path("", views.SteganographyMain, name="SteganographyMainPage"),
    path("fileSubmit/", views.SteganographySubmit, name="SteganographySubmit")
]