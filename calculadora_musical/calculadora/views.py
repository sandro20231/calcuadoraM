from django.shortcuts import render
from .intervalos import tonica, segundamaior, tercamaior, quartajusta, quintajusta, sextamaior, setimamaior, tercamenor, sextamenor, setimamenor

# Create your views here.


def escalamaior(request):
    if request.method == "POST":
        letra = request.POST['le1']
        grau1 = tonica(letra)
        grau2 = segundamaior(letra)
        grau3 = tercamaior(letra)
        grau4 = quartajusta(letra)
        grau5 = quintajusta(letra)
        grau6 = sextamaior(letra)
        grau7 = setimamaior(letra)
        return render(request, 'calculadora/escalamaior.html', {"grau1": grau1,
                                                                "grau2": grau2,
                                                                "grau3": grau3,
                                                                "grau4": grau4,
                                                                "grau5": grau5,
                                                                "grau6": grau6,
                                                                "grau7": grau7})
    return render(request, 'calculadora/escalamaior.html')


def menor(request):
    if request.method == "POST":
        letra = request.POST['le2']
        grau1 = tonica(letra)
        grau2 = segundamaior(letra)
        grau3 = tercamenor(letra)
        grau4 = quartajusta(letra)
        grau5 = quintajusta(letra)
        grau6 = sextamenor(letra)
        grau7 = setimamenor(letra)
        return render(request, "calculadora/menor.html", {
            "grau1": grau1,
            "grau2": grau2,
            "grau3": grau3,
            "grau4": grau4,
            "grau5": grau5,
            "grau6": grau6,
            "grau7": grau7
        })
    return render(request, "calculadora/menor.html")


def menorharmonica(request):
    if request.method == "POST":
        letra = request.POST['le3']
        grau1 = tonica(letra)
        grau2 = segundamaior(letra)
        grau3 = tercamenor(letra)
        grau4 = quartajusta(letra)
        grau5 = quintajusta(letra)
        grau6 = sextamenor(letra)
        grau7 = setimamaior(letra)
        return render(request, "calculadora/menorharmonica.html", {
            "grau1": grau1,
            "grau2": grau2,
            "grau3": grau3,
            "grau4": grau4,
            "grau5": grau5,
            "grau6": grau6,
            "grau7": grau7
        })
    return render(request, "calculadora/menorharmonica.html")


def index(request):
    return render(request, "calculadora/index.html")


def menormelodica(request):
    if request.method == "POST":
        letra = request.POST['le4']
        grau1 = tonica(letra)
        grau2 = segundamaior(letra)
        grau3 = tercamenor(letra)
        grau4 = quartajusta(letra)
        grau5 = quintajusta(letra)
        grau6 = sextamaior(letra)
        grau7 = setimamaior(letra)
        return render(request, "calculadora/menormelodica.html", {
            "grau1": grau1,
            "grau2": grau2,
            "grau3": grau3,
            "grau4": grau4,
            "grau5": grau5,
            "grau6": grau6,
            "grau7": grau7
        })
    return render(request, "calculadora/menormelodica.html")
