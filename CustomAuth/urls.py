#Criamos um novo arquivo de URL dedicado a authenticação e cadastro

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]