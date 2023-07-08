# desafio 60 numero fatorial
num = int(input('digite um número que direi seu fatorial: '))
nufat = int(num)
mult = int(1)
while nufat != 1:
    nufat = nufat - 1
    mult = mult * nufat
    print(f'{nufat}! ')
print(f'O fatorial de seu numero é igual a {mult}')

