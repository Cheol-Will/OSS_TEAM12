from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
def workoutpage(request):
    return render(request, 'workout.html')

def dietpage(request):
    return render(request,'diet.html')

def newspage(request):
    return render(request, 'template.html')

def routine1(request):
    return render(request, 'routine1.html')
def routine2(request):
    return render(request, 'routine2.html')
def routine3(request):
    return render(request, 'routine3.html')
def routine4(request):
    return render(request, 'routine4.html')