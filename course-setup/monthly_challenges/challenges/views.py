from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("This works on February!")

def march(request):
    return HttpResponse("This is actually working on March too!")

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'This works!'
    elif month == 'february':
        challenge_text = 'This works on February!'
    elif month == 'march':
        challenge_text = 'This is actually working on March too!'
    else:
        return 
    return HttpResponse(challenge_text)