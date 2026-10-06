from django.urls import path
from . import views

app_name = "mabio"

urlpatterns = [
    path("", views.indexx, name="index"),
]