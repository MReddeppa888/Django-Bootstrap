from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad(request):

    places = ["Golkonda", "Sanghi", "Charminar", "Chilkur"]
    context = {"places" : places}
    return render(request, "hyderabad2.html", context)

    # return render (request,"hyderabad.html")

    # response="<h1> Welcome to Hyderadad</h1>"
    # return HttpResponse(response)


def warangal(request):
    return render (request,"warangal.html")

    # response="<h1> Welcome to Warangal</h1>"
    # return HttpResponse(response)


