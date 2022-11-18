print('='*50)
print('{:=^}'.format('Supermercado Bom!!'))
print('='*50)
total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    preço = float(input(' Qual o preço? R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa!!'))
print(f' O total da compra foi de R${total}')
print(f'{totmil} produtos custam mais de R$ 1.000,00')
print(f'O nome do produto mais barato é {barato}')
