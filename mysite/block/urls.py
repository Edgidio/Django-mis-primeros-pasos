
from . import views
from django.urls import path

urlpatterns = [
    path('block/<str:parametro>', views.blockk),
    path('', views.index),
]