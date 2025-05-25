from django.shortcuts import render
from .acoes import traduzir_numero

# Create your views here.


def telainicial(request):
    if request.method == "POST":
        letra = request.POST['le1']
        resposta = traduzir_numero(letra)
        return render(request, 'calculadora/tela.html', {"resposta":resposta}) 
    return render(request, 'calculadora/tela.html')
