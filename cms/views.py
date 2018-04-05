from django.shortcuts import render
from django.http import HttpResponse

from .models import Pages

def barra(request):
    lista = Pages.objects.all()
    resp = '<ul>'
    for page in lista:
        resp += '<li>' + str(page.id) + '. ' + page.name
    resp += '</ul>'
    html = '<html><body><h1>Paginas existentes:</h1>' + resp + '</body></html>'
    return HttpResponse(html)

def pagina(request, path):
    try:
        pagina = Pages.objects.get(name=path)
    except Pages.DoesNotExist:
            return HttpResponse("No existe")
    return HttpResponse(pagina.page)
