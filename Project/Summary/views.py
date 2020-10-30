from django.shortcuts import render, redirect, get_object_or_404
from .models import Summary, SummaryText, SummaryNoUser, SummaryTextNoUser
from django.contrib.auth.decorators import login_required

def If_User(request, summary):
    
    if summary.user != request.user:
        return redirect('Home:NotFound')

@login_required
def Get_Summary(request, id):
    summary =  Summary.objects.get(id=id)
    
    If_User(request, summary)
    
    context = {
        'summary':summary
        }
    
    return render(request, 'Summary/GetSummary.html', context)

def Get_Summary_No_User(request, id=id):
    summary = get_object_or_404(SummaryNoUser,id=id)
    
    context ={
        'summary':summary
        }
    
    return render(request, 'Summary/GetSummary.html', context)

def Get_Summary_Text_No_User(request, id=id):
    summary = get_object_or_404(SummaryTextNoUser, id=id)
    
    context = {
        'summary':summary
        }
    
    return render(request, 'Summary/GetSummary.html',context)

@login_required
def Get_Summary_Text(request, id):
    summary = SummaryText.objects.get(id=id)
    
    If_User(request, summary)
    
    context = {
        'summary':summary
        }
    
    return render(request, 'Summary/GetSummary.html',context)