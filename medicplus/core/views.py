from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def QuienesSomos(request):
    return render(request,'Quienessomos.html',{})
