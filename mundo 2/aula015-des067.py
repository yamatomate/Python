# desafio 67 tabuada de um monte de numeros
num = -1
print(f'para fechar o programa digite um  numero negativo \n')
while True:
    num = int(input('deseja ver tabuada de qual numero >> '))
    if num <= 0:
        break
    for c in range(1, 6):
        print(f'{num:=3} x {c:=2} ={num*c:=3} | {num:=3} x {c+5:=2} ={num*(c+5):=3}')
    print('==+==' * 7, '\n')
print('fim')
