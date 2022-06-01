from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def root(request):
    return redirect("/blogs")

def new(request):
    return HttpResponse("Placeholder to display a form to create a new blog")

def blogs(request):
    return HttpResponse("This is blogs page.")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse("placeholder to edit blog number: {number}")

def destroy(request):
    return redirect("/blogs")