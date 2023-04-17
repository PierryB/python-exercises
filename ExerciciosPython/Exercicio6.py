import random
import string

def gen_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.sample(caracteres, tamanho))
    
    return senha

def main():
    tamanho = input("Qual o tamanho da senha desejada? ")
    senha = gen_senha(int(tamanho))
    print(senha)

if __name__ == "__main__":
    main()