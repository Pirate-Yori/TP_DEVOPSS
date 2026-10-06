from django.urls import path
from . import views

app_name = "mabio"

urlpatterns = [
    path("", views.indexx, name="index"),
    path("judicael/", views.index_judi, name="index"),
    
]