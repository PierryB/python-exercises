numero = input("Digite um numero: ")

def calcular(numero):

    if int(numero) % 2 == 0:
        print(numero, "é par")
    else:
        print(numero,"é impar")

calcular(numero)