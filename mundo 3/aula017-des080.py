# desafio 80 ordenado numeros já na posiçao correta
nums = []
ma = me = 0
for c in range(0, 5):
    rep = int(input('digite um numero >>'))
    if c == 0:
        ma = me = rep
    if rep >= ma:
        ma = rep
        nums.append(rep)
        print('adicionado no final')
    elif rep <= me:
        me = rep
        nums.insert(0, rep)
        print('adicionado no começo')
    else:
        for b in range(0, len(nums)):
            if nums[b - 1] < rep < nums[b]:
                print(f'adicionado apos o {nums[b-1]}')
                nums.insert(b, rep)
                break
    # print(f'{rep} <- resposta|lista -> {nums}\n + {ma}\\{me} - ||++ {rep >= ma} ||-- {rep <= me}
    # || nums[b - 1] < rep < nums[b]')
print(f'Sua lista de numeros:\n{nums}')
""" nao existe solução melhor ou mais rapida se ficou diferente do guanabara ,
mas esta rodando corretamente é valida, se ficou maior pode ser um sinal para
ser aprimorada"""