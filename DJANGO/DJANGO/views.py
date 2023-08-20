from django.http import HttpResponse
import datetime

def saludo2 (request):
    return HttpResponse ("Hola Django233")

def diadehoy (request):
    dia = datetime.datetime.now ()
    documentodetexto = f"<h1>Hoy<h1> es día: <br> <h6>{dia}<h6>"
    return HttpResponse (documentodetexto)

def minombrees (request, nombre):
    documentodetexto = f"<h1>Mi nombre es: {nombre}<h1>"
    return HttpResponse (documentodetexto)