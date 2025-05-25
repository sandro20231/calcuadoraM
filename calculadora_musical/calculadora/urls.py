from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("maior/", views.escalamaior, name="escalamaior"),
    path("menor/", views.menor, name="menor"),
    path("menorharmonica/", views.menorharmonica, name="menorharmonica"),
    path("menormelodica/", views.menormelodica, name="menormelodica")
]
