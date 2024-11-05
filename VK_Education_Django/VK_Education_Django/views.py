from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def newQuestion(request):
    return render(request, 'newQuestion.html')

def question(request):
    return render(request, 'question.html')

def searchQuestion(request):
    return render(request, 'searchQuestion.html')

def logIn(request):
    return render(request, 'logIn.html')

def registration(request):
    return render(request, 'registration.html')

def userProfile(request):
    return render(request, 'userProfile.html')