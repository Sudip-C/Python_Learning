from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to Greeting App")

def greet(request,username):
    return HttpResponse(f"Hello, {username}!!")

def farewell(request,username):
    return HttpResponse(f"Goodbye, {username}!!")

# Create your views here.
