from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello world!', content_type="text/plain")
def home_test(request):
    return HttpResponse('Hello world!')
def base(request):
    return render(request, 'static_handler.html')