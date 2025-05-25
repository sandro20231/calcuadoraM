from django.test import TestCase, Client
from .intervalos import traduzir_numero, segundamaior, segundamenor, tercamenor, tercamaior, quartajusta, quintadiminuta, quintajusta, sextamenor, sextamaior, setimamenor, setimamaior
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
    # testa de conexão com tela de escala maior

    def test_telainicial(self):
        c = Client()
        tela = c.get('/maior/')
        self.assertEqual(tela.status_code, 200)

    # teste de conexão com tela de escala menor
    def test_telamenor(self):
        c = Client()
        tela = c.get('/menor/')
        self.assertEqual(tela.status_code, 200)

    # teste de conexão com tela de escala menor harmonica
    def test_telamenorharmonica(self):
        c = Client()
        tela = c.get('/menorharmonica/')
        self.assertEqual(tela.status_code, 200)

    # tetse de conexão com tel de menor melodica

    def test_menormelodica(self):
        c = Client()
        tela = c.get('/menormelodica/')
        self.assertEqual(tela.status_code, 200)

    # testes para intervalos:
    def test_segundamenor(self):
        """segunda menor de c é c#"""
        self.assertEqual(segundamenor("c"), "C#")

    def test_segundamaior(self):
        """segunda maior de B é C#"""
        self.assertEqual(segundamaior("B"), "C#")

    def test_tercamenor(self):
        """terça menor de A é C"""
        self.assertEqual(tercamenor("A"), "C")

    def test_tercamaior(self):
        """terça maior de c é E"""
        self.assertEqual(tercamaior("c"), "E")

    def test_quartajusta(self):
        """quartajusta de c é f"""
        self.assertEqual(quartajusta("c"), "F")

    def test_quintadiminuta(self):
        """quinta diminuta de D é G#"""
        self.assertEqual(quintadiminuta("d"), "G#")

    def test_quintajusta(self):
        """quinta justa de E é B"""
        self.assertEqual(quintajusta("e"), "B")

    def test_sextamenor(self):
        """sexta menor de C é G#"""
        self.assertEqual(sextamenor("c"), "G#")

    def test_sextamaior(self):
        """sexta maior de E é C#"""
        self.assertEqual(sextamaior("e"), "C#")

    def test_setimamenor(self):
        """setima menor de C é A#"""
        self.assertEqual(setimamenor("C"), "A#")

    def test_setimamaior(self):
        """sétima maior de B é A#"""
        self.assertEqual(setimamaior("B"), "A#")
