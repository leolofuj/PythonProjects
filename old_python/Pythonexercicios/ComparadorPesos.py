maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa: Kg '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(' A pessoa mais pesada da lista pesa  {}Kg e a menos pesada  {}Kg'.format(maior, menor))



