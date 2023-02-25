from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'learnURL/homepage.html')

def other(request):
    return render(request,'learnURL/other.html')

def relative(request):
    return render(request,'learnURL/relative.html')

def home(request):
    return HttpResponse("New APP learnURL")