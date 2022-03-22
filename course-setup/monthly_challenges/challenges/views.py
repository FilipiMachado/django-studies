from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month!')
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge")
    return HttpResponseRedirect(redirect_path + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not valid!")