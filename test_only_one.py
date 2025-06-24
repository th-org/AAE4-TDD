import  string

from GeradorDeSenhas import gerar_senha


def test_only_one_character():
    senha = gerar_senha(8, True, True, True, True)
    if not any(c in string.punctuation and string.ascii_lowercase and string.ascii_uppercase and  c in string.digits  for c in senha):
        print("A senha deve conter pelo menos um caractere de cada.")
        return False
    return True
