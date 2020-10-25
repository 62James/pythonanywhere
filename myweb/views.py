from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate

def logout(req):
    logout_user(req)
    return redirect('login')

def index(req):
	return render(req, 'myweb/index.html')

def united(req):
	return render(req, 'myweb/united.html')

def home(req):
    return render(req, 'myweb/home.html')

#def login(req):
 #   return render(req, 'myweb/login.html')

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'myweb/detail.html',{'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


#def login_page(request):
 #   return render(request,'myweb/index.html')

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def register(req):
    return render(request ,'myweb/register.html')

def login_Web(req):
    return render(request ,'myweb/Login.html')

def logout(req):
    logout_user(req)
    return redirect('login')

def register(request):
    return render(request ,'myweb/register.html')

def  recipes_details1(request):
    return render(request,'myweb/recipes_details1.html')

def  recipes_details2(request):
    return render(request,'myweb/recipes_details2.html')

def  recipes_details3(request):
    return render(request,'myweb/recipes_details3.html')

def  recipes_details4(request):
    return render(request,'myweb/recipes_details4.html')

def  recipes_details5(request):
    return render(request,'myweb/recipes_details5.html')

def  recipes_details6(request):
    return render(request,'myweb/recipes_details6.html')


