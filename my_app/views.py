from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# Create your views here.

def home(request):
    context = {}
    title = 'home'
    context['title'] = title
    return render(request,'home.html',context)

def login_view(request):
    context = {}
    title = 'login'
    context['title'] = title

    if request.method == 'POST':
        form_data = LoginForm(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']

            user = authenticate(
                request,username=username,password=password
            )
            
            if user :
                auth_login(request,user)
                messages.success(
                    request,'login successful'
                )
                return redirect('home')
            else :
                messages.error(
                    request,'invalid credentials'
                )
                return redirect(title)
                

    form_data = LoginForm()
    context['form_data'] = form_data
    return render(request,'login.html',context)

def logout_view(request):
    auth_logout(request)
    return redirect('login')