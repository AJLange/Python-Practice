from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Response from index method from root route, localhost!")

def root(request):
    return HttpResponse("return to root")

def new_route(request):
    return HttpResponse("Response from index method from root route, localhost!")

def blogs(request):
    return HttpResponse("This is blogs page.")