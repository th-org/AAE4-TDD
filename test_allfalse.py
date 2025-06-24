import unittest
from GeradorDeSenhas import gerar_senha, senhaError

class GeradorDeSenhasTesteCase(unittest.TestCase):
    def test_all_false(self):
        with self.assertRaises(senhaError):
            gerar_senha(tamanho=10, incluir_maiusculas=False, incluir_minusculas=False, incluir_numeros=False, incluir_simbolos=False) 

if __name__ == '__main__':
    unittest.main()
