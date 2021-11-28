from django.shortcuts import render
from main import *

# Create your views here.

def workoutpage(request):
    return render(request, 'workout.html')