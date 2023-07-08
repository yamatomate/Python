# desafio 78 uma lista de 5 num e diga quem é o maior e o menor
nums = [int(input('digite um numero >>')), int(input('digite outro numero >>')),
        int(input('digite mais outro numero >>')), int(input('digite novamente um numero >>')),
        int(input('por fim digite um numero >>'))]
print(f'Os numeros digitados são {nums}')
ma = me = nums[0]
poe = poa = 0
for c in range(0, len(nums)):
    if nums[c] > ma:
        ma = nums[c]
        poa = c
    elif nums[c] < me:
        me = nums[c]
        poe = c
print(f"o maior numero foi {ma} que fica na posição", end="")
for a in range(0, len(nums)):
    if nums[a] == ma:
        print(f' ->{a+1}', end="")
print(f"\no menor numero foi {me} que fica na posição", end="")
for a in range(0, len(nums)):
    if nums[a] == me:
        print(f' ->{a+1}', end="")
