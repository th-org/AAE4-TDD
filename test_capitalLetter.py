from GeradorDeSenhas import gerar_senha

def test_capital_letter():
    senha = gerar_senha(8, True)
    if not any(c.isupper() for c in senha):
        print("A senha precisa conter ao menos uma letra maiúscula")
        return False
    return True
