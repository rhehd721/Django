from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')
# Create your views here.
