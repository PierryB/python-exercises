from random import randint
from time import sleep
computador = randint(1, 9)
while True:
    jogador = input('Digite um número entre 1 e 9 (Digite "sair" para sair do programa): ')
    sleep(1)
    bool = any(char.isalpha() for char in jogador)

    if jogador.upper().find('SAIR') != -1:
        print('Saindo...')
        sleep(1)
        break
    elif bool is True:
        print('O texto digitado não é um número!')
        sleep(1)
        print('Saindo...')
        sleep(1)
        break
    elif computador == int(jogador):
        print('O número digitado "{}" é o correto!'.format(jogador))
    elif computador < int(jogador):
        print('O número digitado "{}" é maior que o número escolhido"'.format(jogador))
    elif computador > int(jogador):
        print('O número digitado "{}" é menor que o número escolhido!'.format(jogador))
    else:
        print('Opção Inválida!')