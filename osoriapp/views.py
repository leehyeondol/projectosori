from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def annonyboard(request):
    return render(request,'anonyboard.html')

def fashionboard(request):
    return render(request,'fashionboard.html')