from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import F1ResultModels
from django.http import HttpResponse

@api_view(['GET'])
def mostrar(request):
    f1resutado = F1ResultModels.objects.all()
    conteudo = {
        'corridas': f1resutado
    }
    return render(request,'mostrar.html', conteudo)


def formulario(request):
    return render(request,'buscar.html')


def busc(request):
    formulario(request)
    if request.method == 'POST':
        ano = request.POST.get('ano')
        return render(request,'mostrar.html')
    else:
        return HttpResponse('Método não suportado')

   
    


    