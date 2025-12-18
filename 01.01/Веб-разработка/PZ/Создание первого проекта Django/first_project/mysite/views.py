from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Привет, МИР!</h1>")

def second_page(requqest):
    return render(requqest, template_name='2page.html')

def page1(request): return render(request, 'page1.html')
def page2(request): return render(request, 'page2.html')
def page3(request): return render(request, 'page3.html')
def page4(request): return render(request, 'page4.html')
def page5(request): return render(request, 'page5.html')