# desafio 66 varios numeros com flag
ss = qq = 0
print('digite 999 para parar.')
while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    ss += num
    qq += 1
# fim
print(f'a soma entre os numeros são {ss} e {qq} numeros foram digitados')
