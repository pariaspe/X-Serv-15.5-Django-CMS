from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    html = '<html><body><h1>Hello world!</h1></body></html>'

    return HttpResponse(html)
