a = int(input('Digite o valor do 1º termo da PA: '))
r = int(input(' Digite a razão da PA: '))
n = int(input('Digite o número de termos da PA: '))
ultimo = a + (n - 1) * r
for c in range(a , ultimo, r):
    print(c , end=' - ')
print('PA')







