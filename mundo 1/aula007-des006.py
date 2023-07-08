# desafio 7 dobro triplo e raiz quadrado
"""num = int(input(digite um numero: '))"""
from random import randint

num = randint(1, 100)
dob = num*2
tri = num*3
rai = num**(1/2)
print(f'numero={num}\ndobro={dob}\ntriplo={tri}\nraiz={rai:.2f} (aprox)')
