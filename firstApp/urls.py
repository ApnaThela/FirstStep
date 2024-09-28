from django.urls import path

from . import views

urlpatterns = [
    path('', views.Responder3),
    path('<int:name>', views.Responder2),
    path('<str:name>', views.Responder, name="stringArg")
    ]