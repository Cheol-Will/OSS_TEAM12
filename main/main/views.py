from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
def workoutpage(request):
    return render(request, 'workout.html')

def dietpage(request):
    return render(request,'diet.html')

def newspage(request):
    return render(request, 'template.html')