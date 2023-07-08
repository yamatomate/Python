# desafio 29 multa de carro
# velo = float(input('a quantos km/h tava o carro: '))
from random import randint

velo = randint(1, 240)
if velo >= 80:
    exden = (velo - 80)
    multa = 7 * exden
    print(f'A multa a se paga por esse carro é de {multa:.2f} Bolsonaros por andar a {velo}')
else:
    print('esta dentro do limite continue assim')
print('80km é limite de velocidade')
print(velo, exden)
