# desafio 79 cadastrando varios numeros sem repetir
nums = []
while True:
    resp = int(input('|| Digite um numero >>'))
    if resp not in nums:
        nums.append(resp)
    else:
        print('X valor duplicado, não sera adicionado X')
    opc = str(input('deseja continuar \\S\\N\\ -> '))
    if opc.upper().strip() in 'N':
        break
    # print(resp, "<- respota | lista ->", nums)
print('=-='*10, f'\nA lista dos numeros digitados em ordem cresente:\n {sorted(nums)}')
