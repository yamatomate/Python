#lista de pares e impares
from random import randint
numes = [[], []]
for c in range(0, 7):
    # num = int(input("digite um numero >> "))
    num = int(randint(1, 30))
    if num%2 == 0:
        numes[0].append(num)
    else:
        numes[1].append(num)
numes[0].sort()
numes[1].sort()
print(f'Os pares organizado:\n{numes[0]}')
print(f'Os impares organizado:\n{numes[1]}')
