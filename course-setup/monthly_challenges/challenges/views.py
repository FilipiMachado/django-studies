from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "This works",
    "february": "This works on February!",
    "march": "This is actually working on March too!",
    "april": "This works",
    "may": "This works on February!",
    "june": "This is actually working on March too!",
    "july": "This works",
    "august": "This works",
    "september": "This works on February!",
    "october": "This is actually working on March too!",
    "november": "This works",
    "december": "This works on February!",
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = monthly_challenges.keys()
    redirect_month = months[month]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not valid!")