from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from main import *
# Create your views here.

def user_create(request) :
    if request.method== "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request, user)
            return redirect('main:views:index')
    else : # 회원가입 페이지 첫 접근
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'signup.html', context)

def user_login(request) : 
    if request.user.is_authenticated :
        return redirect('main:index')
    if request.method=='POST' :
        form = AuthenticationForm(request, data = request.POST) 
        if form.is_valid() :
            auth_login(request, form.get_user())
            return redirect('main:index') # 로그인 성공시 메인페이지 이동
    else :
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'login.html', context)

@require_POST
def user_logout(request) :
    auth_logout(request)
    return redirect('main:index')

