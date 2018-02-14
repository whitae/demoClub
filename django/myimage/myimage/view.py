from django.shortcuts import render
def hello(request):
    ctx={}
    return render(request,"index.html",ctx)
