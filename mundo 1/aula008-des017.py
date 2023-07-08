# desafio 17 sen cos e tag de qualquer angulo
from math import pow, sqrt
catop = float(input('cateto oposto: '))
catad = float(input('cateto adjacente: '))
"""catop = float(3)
catad = float(4)"""
hipo = sqrt((pow(catop, 2)+pow(catad, 2)))
print(f'a hipotenusa de seu triangulo retangulo é igual a {hipo}')
