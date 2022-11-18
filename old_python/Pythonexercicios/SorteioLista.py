from random import randint
from time import sleep
def sorteio(lista):
    print('Os números sorteados foram: ', end='')
    for c in range(0, 5):
        s = randint(1, 10)
        lista.append(s)
        print(f'{s}.. ', end='')
        sleep(0.3)
    print('FIM!!')

def somapar(lista):
    contpar = 0
    for c in lista:
        if c % 2 == 0:
            contpar += c
    print(f' Na lista {lista} a soma dos números pares é igual a {contpar} .')


numeros = list()
sorteio(numeros)
#print(f'A lista formada com o sorteio foi {numeros}', end='')
somapar(numeros)
