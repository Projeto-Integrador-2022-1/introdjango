from django.urls import path

from formsexemplo import views

urlpatterns = [
    path('', views.home, name="index_formexemplo"),
]