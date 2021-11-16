from django.shortcuts import render

# Create your views here.

def newspage(request):
    return render(request, 'template.html')