import unittest
from GeradorDeSenhas import gerar_senha

class GeradorDeSenhasTesteCase(unittest.TestCase):
    def test_all_false(self):
        gerador = gerar_senha(tamanho=10, incluir_maiusculas=False, incluir_minusculas=False, incluir_simbolos=False)
        gerador.gerador()

if __name__ == '__main__':
    unittest.main()
