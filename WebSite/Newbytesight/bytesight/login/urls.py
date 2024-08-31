from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginPage, name="LoginPage"),
    path("submit", views.LoginSubmit, name="LoginSubmit")
]