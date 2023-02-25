from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import User
from firstapp.forms import NewformPage
from . import forms


def home(request):
    return render(request,'home.html')

def homepage(request):
    return HttpResponse("Welcome to Django Development")

def index(request):
    mydict = {'insert':"Inserted from views"}
    return render(request,'index.html',context=mydict)
def help(request):
    mydict = {'insert':"User is Registered"}
    return render(request,'help.html', context=mydict)

def users(request):

    users_list = User.objects.order_by('fname')
    dict = {"User_Data":users_list}
    return render(request,'users.html',context=dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':

        form = forms.FormName(request.POST)
        if form.is_valid():
            print('NAME:'+form.cleaned_data['name'])
            print('EMAIL:'+form.cleaned_data['email'])

    return render(request,'forms/form_page.html',{'form':form})

def formdataSave(request):

    user = forms.NewformPage()

    if request.method == 'POST':
        user = NewformPage(request.POST)
        if user.is_valid():
            user.save(commit=True)
            return index(request)
        else:
            print("Invalid user")

    return render(request,'forms/form_page.html',{'form':user})