
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "myApp/home.html")

def page2(request):
    return render(request, "myApp/Page2.html")

def page3(request):
    return render(request, "myApp/Page3.html")

def page4(request):
    return render(request, "myApp/Page4.html")

def page5(request):
    return render(request, "myApp/Page5.html")