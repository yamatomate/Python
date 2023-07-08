# desafio 96 calculo da area
def area(x, y):
    s = x * y
    print(f'A área {x} x {y} = {s} M^2')


print('{:^50}\n'.format('Controle de terrenos'), '=' * 50)
larg = float(input(" Qual a largura de seu terreno (em M): "))
altu = float(input(" Qual o comprimento de seu terreno (em M): "))
area(larg, altu)
