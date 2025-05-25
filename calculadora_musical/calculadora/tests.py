from django.test import TestCase, Client
from .acoes import traduzir_numero
# Create your tests here.


class testes(TestCase):
    # testes de tradução de letras em números
    def testenota1(self):
        """C é 1"""
        self.assertEqual(traduzir_numero("C"), 1)

    def testnota2(self):
        """d é 3"""
        self.assertEqual(traduzir_numero("d"), 3)

    def testnota3(self):
        """F# é 7"""
        self.assertEqual(traduzir_numero("F#"), 7)

    def testnota4(self):
        """g# é 9"""
        self.assertEqual(traduzir_numero("g#"), 9)

    def testnota5(self):
        """Gb é 7"""
        self.assertEqual(traduzir_numero("Gb"), 7)

    def testnota6(self):
        """ab é 9"""
        self.assertEqual(traduzir_numero("ab"), 9)
    # testa de conexão com tela incial

    def test_telainicial(self):
        c = Client()
        tela = c.get('')
        self.assertEqual(tela.status_code, 200)
