from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.getAllTransactions, name="getAllTransactions"),
]