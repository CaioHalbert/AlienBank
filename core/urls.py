"""alienbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [ #Adiciona as urls que serão usadas na aplicação

    path("", TemplateView.as_view(template_name="home.html"), name="home"), # Chama diretamente a pagina home, independente de logica criada para index

    path('admin/', admin.site.urls), # Inclui app admin no projeto como acessivel

    path("accounts/", include("CustomAuth.urls")), # Inclui um camino para as urls da app CustomAuth

    path("transactions/", include("transaction.urls")),

    path("accounts/", include("django.contrib.auth.urls")), # Inclui as validações da app auth

]
