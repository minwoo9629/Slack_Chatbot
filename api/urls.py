from django.contrib import admin
from django.urls import path, include
from api import views

app_name = 'api'
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name="hello"),
]
