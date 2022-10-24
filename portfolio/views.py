from django.shortcuts import render

# Create your views here.\

def index(request):
    context = {}
    return render(request, 'portfolio/index.html',context)

def resume(request):
    context = {}
    return render(request, 'portfolio/resume.html',context)
