from GeradorDeSenhas import gerar_senha

def test_lowercase_letter():
    senha = gerar_senha(8, True, True)
    if not any(c.islower() for c in senha):
        print("A senha precisa conter ao menos uma letra minúscula")
        return False
    return True
