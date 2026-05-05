from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad(request):
    return render (request,"hyderabad.html")

    # response="<h1> Welcome to Hyderadad</h1>"
    # return HttpResponse(response)


def warangal(request):
    return render (request,"warangal.html")

    # response="<h1> Welcome to Warangal</h1>"
    # return HttpResponse(response)


