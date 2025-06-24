import random
import string

def gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    try {
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase

        if incluir_minusculas:
            caracteres += string.ascii_lowercase

        if incluir_numeros:
            caracteres += string.digits

        if incluir_simbolos:
            caracteres += string.punctuation

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha
    }catch{
        if not any([self.tamanho, self.incluir_maiusculas, self.incluir_minusculas, self.incluir_numeros, self.incluir_simbolos]):
            raise PasswordCriteriaError("Pelo menos um critério deve ser selecionado.")
    }


if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        senha = gerar_senha(tamanho, incluir_maiusculas=True, incluir_minuscula=True, incluir_numeros=True, incluir_simbolos=True)
        print(f"Senha gerada: {senha}")
    except ValueError as e:
        print(f"Erro: {e}")
