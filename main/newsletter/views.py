from django.shortcuts import render
from main import *

# Create your views here.

def newspage(request):
    return render(request, 'template.html')