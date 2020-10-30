from django.shortcuts import redirect
from urllib.request import urlopen
from .summarize import Summarize, Summarize_Text
from .models import Summary, SummaryText, SummaryNoUser, SummaryTextNoUser
from urllib.error import HTTPError

def Access(url,my_user):
    try:
        urlopen(url)
        summary = Summarize(url)
        if my_user != None:
            Summary.objects.create(user=my_user, link=url, text=summary)
        else:
            SummaryNoUser.objects.create(link=url, text=summary)
    except (ValueError, HTTPError):
        return redirect('Home:NotFound')

def Access_Text(text, my_user):
    summary = Summarize_Text(text)
    if my_user != None:
        SummaryText.objects.create(user=my_user,text=summary)
    else:
        SummaryTextNoUser.objects.create(text=summary)
    
    return summary