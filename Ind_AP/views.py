from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chittoor(request):
    return render (request,"chittoor.html")

    # response="<h1> Welcome to Chittoor</h1>"
    # return HttpResponse(response)


def kadapa(request):
    return render (request,"kadapa.html")

    # response="<h1> Welcome to Kadapa</h1>"
    # return HttpResponse(response)



