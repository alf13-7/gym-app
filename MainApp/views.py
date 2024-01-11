from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def beginning_page_redirect(request):
    if request.user.is_authenticated:
        # return HttpResponse("You are authenticated!")
        return render(request, 'home_page.html')
    else:
        # return HttpResponse("You are not authenticated!")
        return redirect("/log-in")
