lista = list()
pares = list()
ímpar = list()
c = ''
while c in 'S':
    n = int(input(' Digite um valor: '))
    c = str(input(' Quer continuar?[S/N] ')).strip().upper()[0]
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        ímpar.append(n)

print(f'Esta é a lista digitada: {lista}')
print(f' Estes são os números pares da lista: {pares}')
print(f'Estes são os números ímpares: {ímpar}')
print(f'Esta é a lista com todos os elementos: {lista + pares + ímpar}')
print('Fim!!')
