from django.urls import path, include
from . import views

app_name = "search"

urlpatterns = [
    path('', views.index, name = "pic_search"),
    path('auth/', views.auth, name = "pic_auth"),
    path('show/', views.show, name = "pic_show"),
]
