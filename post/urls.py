from django.urls import path, include
from . import views

app_name = "post"

urlpatterns = [
    path('', views.get_img, name = "img_get"),
]
