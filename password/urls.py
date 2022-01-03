

from django.urls import path
from .views import hw,passwordgenerator,fetchdetails

urlpatterns = [
    path("main/passwordscape/", hw, name="hw"),
    path('main/passwordscape/generate',passwordgenerator,name="generate"),
    path("main/passwordscape/history", fetchdetails, name="hist"),

]
