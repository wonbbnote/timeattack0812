from django.contrib import admin
from django.urls import path
from .views import SubscribeView


urlpatterns = [
    path('', SubscribeView.as_view()),
]
