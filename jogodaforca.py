import time

import funcoes as func

frutas = ['Banana', 'Melão', 'Laranja', 'Maçã']
objetos = ['Cama', 'Mesa', 'Cadeira', 'Janela']
cores = ['Azul', 'Amarelo', 'Roxo', 'Verde']

TEMAS: list = ['1', '2', '3']
palavra: str = ''
letras_a_adivinhar: list = []
letras_acertadas: list = []
letras_erradas: list = []

tentativas = 15

func.apresentacao()

while tentativas > 0:

    # Possibilidade de Sair do Jogo digitando Sair:
    print('Você pode Sair do Jogo digitando "SAIR"')
    print()

    # Escolha do tema a ser jogado:
    tema = func.escolha_tema()
    print()

    # Logica da digitação SAIR do jogo:
    if tema.upper() == 'SAIR':
        print('Saindo...')
        time.sleep(2)
        print('By')
        break

    # Se o tema não estiver na lista de temas:
    elif tema not in TEMAS:
        print('Por Favor escolha um tema válido')
        print('#' * 50)
        time.sleep(2)
        continue

    # Se o tema estiver na lista de temas:
    elif tema in TEMAS:
        print('Carregando...')
        time.sleep(2)

        # Apresentação do tema escolhido:
        if tema == '1':
            palavra = func.palavra_adivinhar(frutas)
            print('Você escolheu o Tema "Frutas"')
        elif tema == '2':
            palavra = func.palavra_adivinhar(objetos)
            print('Você escolheu o Tema "Objetos"')
        elif tema == '3':
            palavra = func.palavra_adivinhar(cores)
            print('Você escolheu o Tema "Cores"')

        # Maquina escolhendo o nome de acordo com o tema:
        print('Estou Selecionando um Nome...')
        time.sleep(3)
        print('OK, Pedemos começar...')
        time.sleep(3)

        # Colocando as letras da palavra selecionada em uma lista:
        for letra in palavra:
            letras_a_adivinhar.append(letra)

        while True:
            # Apresentando as letras erradas e escondendo a palavra do desafio:
            print('#' * 100)
            print(f'Você errou essas letras: {letras_erradas}')
            palavra_escondida = func.palavra_parcial(palavra, letras_acertadas)
            print()
            print(f'-----> {palavra_escondida} <-----')
            print()
            print(f'Você tem {tentativas} tentativas')

            if palavra_escondida == letras_a_adivinhar:
                print('Parabéns!!! Você acertou nome que selecionei :D')
                print()
                reiniciar = input('Dejesa Jogar Novamente? "SIM" ou "NAO"')
                if reiniciar.upper() == 'SIM':
                    tentativas = 15
                    letras_erradas = []
                    letras_acertadas = []
                    break
                else:
                    print('OK, até a próxima!')
                    break

            # Entrada de letras do usuário:
            entrada = input('Digite uma letra: ')

            # lógica do jogo:
            if entrada.upper() == 'SAIR':
                break
            elif entrada not in palavra:
                print(f'A letra {entrada}, não está na palavra :( ')
                print()
                letras_erradas.append(entrada)
                tentativas -= 1
                continue
            elif entrada in palavra:
                print(f'A letra {entrada}, está na palavra :) ')
                letras_acertadas.append(entrada)
                tentativas -= 1
                print()

            # Se o numero de tentativas chegar a 0:
        if tentativas == 0:
            print('Suas tentativas acabaram :( ')
            print()

            retry = input('Você deseja tentar novamente?\
                            \n "Sim" ou "Nao"')
            # Possibilidade de tentar novamente:
            if retry.upper() == 'NAO':
                break
            elif retry == 'SIM':
                tentativas == 15
                letras_erradas == []
                letras_acertadas = []
