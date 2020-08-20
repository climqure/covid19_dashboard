from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'mysite/index.html')

def handler404(request, exception):
    context = {}
    return render(request, "mysite/404.html", context)

def handler500(request, exception):
    context = {}
    return render(request, "mysite/404.html", context)