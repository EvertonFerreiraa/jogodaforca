def apresentacao():
    """
    Função que formata a aprentação do jogo no terminal
    """
    import os
    os.system('cls')
    print('#' * 100)
    print('----- BEM VINDO AO JOGO DA FORCA -----')
    print('#' * 100)
    print()
    print('INSTRUÇÕES:\n-Vou selecionar um nome de acordo com o tema.\
        \n-O desafio é descobrir esse nome com as letras do alfabeto.\
        \n-Você tem 15 tentativas para acertar.')
    print()
    print('Boa Sorte!')
    print()


def escolha_tema():
    """
    Função que apresenta as opções de temas para o usuário escolher
    -> str 1 (Frutas), 2 (Objetos) ou 3 (Cores)
    """
    print()
    entrada = input('Escolha uma Opção\n[1] Frutas\n[2] Objetos\n[3] Cores\n')

    return entrada


def palavra_adivinhar(lista: list) -> str:
    """
    Função que seleciona uma palavra em uma lista.
    """
    import random
    palavra = random.sample(lista, 1)
    _palavra_adivinhar = palavra[0]
    return _palavra_adivinhar


def palavra_parcial(palavra: str, letras_acertadas: list):
    """
    Função retorna a palavra a adivinhar formatada
    """
    letras: list = []
    for letra in palavra:
        if letra not in letras_acertadas:
            letras.append('_')
        elif letra in letras_acertadas:
            letras.append(letra)
    return letras


if __name__ == '__main__':
    p = palavra_adivinhar(['Everton', 'Milena'])
    print(p)
    print()
    palavra = palavra_parcial(p, ['a', 'e', 'i', 'o', 'u'])
    print(palavra)
