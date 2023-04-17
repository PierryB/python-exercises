from time import sleep

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('Valor adicionado na lista!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        print('Saindo...')
        sleep(1)
        break

lista = remove_repetidos(lista)
print('Lista de números sem os duplicados:')
print (lista)