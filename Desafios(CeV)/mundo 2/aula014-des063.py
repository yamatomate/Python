# desafio 63 sequencia de fibonacci
n = int(input('quantos numeros da sequencia de fibonacci deseja ver: '))
x = 0
y = 1
fi = 0
for c in range(1, n):
    x = fi
    print(f'{fi}; ', end='')
    fi = fi + y
    y = x
