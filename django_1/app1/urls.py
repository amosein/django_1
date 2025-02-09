from django.urls import path
from . import views


urlpatterns = [
    path("salam/", views.say_hello),
]