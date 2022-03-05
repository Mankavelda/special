from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>See na, it works</h1> <p>Hello world</p>")


def findex(request):
    return render(request, "index.html")