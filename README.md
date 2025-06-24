# Gerador de Senhas - Projeto TDD

Este projeto foi desenvolvido para a disciplina de Testes de Software, utilizando a abordagem de Desenvolvimento Orientado a Testes (TDD). O objetivo é criar um gerador de senhas personalizável e garantir sua qualidade por meio de testes automatizados.

## Funcionalidades

- Geração de senhas com tamanho definido pelo usuário
- Opção de incluir letras maiúsculas, minúsculas, números e caracteres especiais
- Validação dos critérios de senha por meio de testes automatizados

## Estrutura do Projeto

- `GeradorDeSenhas.py`: Implementação da função principal de geração de senhas.
- Arquivos `test_*.py`: Testes automatizados para cada critério de senha, cobrindo:
  - Comprimento da senha
  - Inclusão de letras maiúsculas
  - Inclusão de letras minúsculas
  - Inclusão de números
  - Inclusão de caracteres especiais
  - Garantia de pelo menos um caractere de cada tipo
  - Comportamento quando nenhum critério é selecionado

## Sobre TDD

O projeto foi desenvolvido seguindo o ciclo TDD:

1. Escrever um teste que falha
2. Implementar o código para passar no teste
3. Refatorar e melhorar o código
