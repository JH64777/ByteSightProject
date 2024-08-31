from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignupPage, name="SignupPage"),
    path("check", views.CheckID, name="Check"),
    path("submit", views.AddAccount, name="AddAccount"),
]