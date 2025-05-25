from django.urls import path
from . import views

urlpatterns = [
    path("maior/", views.escalamaior, name="escalamaior"),
    path("menor/", views.menor, name="menor")
]
