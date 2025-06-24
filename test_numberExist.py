from GeradorDeSenhas import gerar_senha

numeros_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def test_exist_number():
    senha = gerar_senha(15, True, True, True)
    if not any(c in numeros_validos for c in senha):
        print("A senha deve conter ao menos um número válido.")
        return False
    return True
