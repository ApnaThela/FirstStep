from django.urls import path

from . import views

urlpatterns = [
    path('<int:name>', views.Responder2),
    path('<str:name>', views.Responder)
    ]