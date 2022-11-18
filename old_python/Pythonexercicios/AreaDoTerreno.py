def area(l, c):
    s = l * c
    print(f'A área do terreno de {l}m por {c}m  é igual a : {s:.2f} m²')


print('-='*20)
l = float(input('Qual a largura do terreno?  '))
c = float(input('Qual o comprimento do terreno?  '))
area(l, c)
