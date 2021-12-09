from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.RandomWord.as_view()),
    path('next/<int:pk>', views.NextWord.as_view()),
]
