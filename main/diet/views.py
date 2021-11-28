from django.shortcuts import render
from main import *

# Create your views here.

def dietpage(request):
    return render(request,'diet.html')