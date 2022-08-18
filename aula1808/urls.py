from django.urls import path

from aula1808 import views

urlpatterns = [
    path('', views.home, name="home1808"),
]
