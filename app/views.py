from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def  ravi(request):
    return HttpResponse("<marquee> <h1>i want job as developer</h1> </marquee>")
def hr(request):
    return HttpResponse("<marquee><h1>Congratulations</h1> </marquee>")