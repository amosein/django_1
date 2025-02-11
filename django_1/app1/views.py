from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    all = Todo.objects.all()
    return render(request, "home.html", context={"all": all})

def say_hello(request):
    person = {"name": "admin", "last_name": "Razavi"}
    return render(request, "hello.html", context=person)