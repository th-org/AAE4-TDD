from GeradorDeSenhas import gerar_senha

def test_word_length_valid():
    for tamanho in [0, 1, 5, 10, 16, 32]:
        assert len(gerar_senha(tamanho)) == tamanho

