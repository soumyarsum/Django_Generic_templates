from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a(request):
    return HttpResponse("<marquee><h1>Code is working..</h1></marquee>")
def b(request):
    return render(request, "csk.html")
