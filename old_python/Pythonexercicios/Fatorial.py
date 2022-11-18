def fatorial(n, show=False):
    fat = 1
    print('-' * 30)
    print('O fatorial do número é: ', end='')
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat





num = int(input('Digite um valor para ver seu fatorial: '))
print(fatorial(num, False))
