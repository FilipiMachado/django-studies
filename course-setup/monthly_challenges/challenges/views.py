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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month!')
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound("<h1>This month is not valid!</h1>")
    