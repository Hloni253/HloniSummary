from django.shortcuts import render, redirect
from Summary.models import Summary, SummaryText, SummaryNoUser, SummaryTextNoUser
from Summary.access_url import Access, Access_Text
from Summary.summarize import Summarize_Text

def Summary_Query(summary_q):
    if summary_q.exists():
        summary = summary_q.first()
    else:
        return redirect('Home:NotFound')
    
    return summary

def Home(request):
    if request.user.is_authenticated:
        my_user = request.user
        summaries = Summary.objects.filter(user=my_user)
        summaries_text = SummaryText.objects.filter(user=my_user)
    else:
        my_user = None
        summaries = None
        summaries_text = None
    if request.method == "POST":
        if request.POST.get('link'):
            url = request.POST.get('link')
            Access(url,my_user)
            if my_user != None:
                summary_q = Summary.objects.filter(link=url)
                summary = Summary_Query(summary_q)
                return redirect('Summary:Get Summary', summary.id)
            else:
                summary_q = SummaryNoUser.objects.filter(link=url)
                summary = Summary_Query(summary_q)
                return redirect('Summary:Get Summary No User', summary.id)
        elif request.POST.get('text'):
            full_text = request.POST.get('text')
            summarized_text = Access_Text(full_text, my_user)
            if my_user != None:
                summary_q = SummaryText.objects.filter(text=summarized_text)
                summary = Summary_Query(summary_q)
                return redirect('Summary:Get Summary Text', summary.id)
            else:
                summary_q = SummaryTextNoUser.objects.filter(text=summarized_text)
                summary = Summary_Query(summary_q)
                return redirect('Summary:Get Summary Text No User', summary.id)
    else:
        pass
    
    context = {
        'my_user':my_user,
        'sums':summaries,
        'sums_t':summaries_text
        }

    return render(request, 'Home/Home.html', context)


def Link_Not_Found(request):
    return render(request, 'Home/NotFound.html')