from turtle import forward
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This works!",
    "february": "This works on February!",
    "march": "This is actually working on March too!",
    "april": None,
    "may": "This works on February!",
    "june": "This is actually working on March too!",
    "july": "This works",
    "august": "This works",
    "september": "This works on February!",
    "october": "This is actually working on March too!",
    "november": "This works",
    "december": None,
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
      "months": months,
    })

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
            "title": month
        })
    except:
        raise Http404()
    