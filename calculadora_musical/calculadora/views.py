from django.shortcuts import render

# Create your views here.


def telainicial(request):
    return render(request, 'calculadora/tela.html')
