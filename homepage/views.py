from django.shortcuts import render

def index(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def signup(request):
    return render(request, 'homepage/signup.html')

