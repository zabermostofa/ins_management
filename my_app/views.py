from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def home(request):
    context = {}
    title = 'home'
    context['title'] = title
    return render(request,'home.html',context)