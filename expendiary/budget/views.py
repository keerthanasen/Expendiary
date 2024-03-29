from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'list.html')

def description(request, project_slug):
    return render(request, 'description.html')