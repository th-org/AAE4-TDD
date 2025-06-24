import  string

from GeradorDeSenhas import gerar_senha

def test_special_character():
    senha = gerar_senha(8, True, True, True, True)
    if not any(c in string.punctuation for c in senha):
        print("A senha deve conter pelo menos um caractere especial.")
        return False
    return True
