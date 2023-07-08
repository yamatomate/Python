"""desenvolva um programa que pergunte a distancia de uma viagem
 em Km. calcule o preço , combranndo R$0,50 por Km para viagens
 de ate 200Km e R$0,45 para vaigens mais longas"""
# desafio 31 preço de viagem
# dist = int(input('quantos KM você precisa percorrer para chegar ao seu destino: '))
from random import randint

dist = randint(1, 500)
if dist <= 200:
    preco = float(dist * 0.50)
    print(f'sua vaigem tem menos de 200km então pagara: {preco:.2f} bolsonaros')
else:
    preco = float(dist * 0.45)
    print(f'sua viagem tem mais de 200km então pagara: {preco:.2f} bolsonaros')
print(f'distacia:{dist}Km\n-fim-')
