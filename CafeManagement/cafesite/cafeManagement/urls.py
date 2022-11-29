from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acList),
    path('form/', views.acForm),
    path('delete/', views.acDelete),
    path('update/', views.acUpdate),
    path('view/', views.acView),
    path('login/',views.acLogin)
]