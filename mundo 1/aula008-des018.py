# desafio 18 do sen cos tag de um angulo qualquer
from math import radians, sin, cos, tan
# ang = float(input('de um angulo para calular o sen, cos e a tag: '))
ang = float(30)
angrad = radians(ang)
sen = sin(angrad)
cose = cos(angrad)
tag = tan(angrad)
print(f'o angulo {ang} possui:\nseno:{sen:.4f}\ncoseno:{cose:.4f}\ntagente:{tag:.4f}')





