import  string

from GeradorDeSenhas import gerar_senha

numeros_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def test_only_one_character():
    senha = gerar_senha(8, True, True, True, True)
    if not any(c in string.punctuation & c.islower() & c.isupper &  c in numeros_validos  for c in senha):
        print("A senha deve conter pelo menos um caractere de cada.")
        return False
    return True
