# desafio 7 media aritimetica de um aluno
"""not1 = float(input('qual a primeira nota: '))
not2 = float(input('qual a segunda nota: '))"""
from random import randint
not1 = randint(0, 10)
not2 = randint(0, 10)
med = ((not1+not2)/2)
print(f'A primeira nota:{not1} e a segunda nota:{not2} e a media das provas são:')
print(f'{med:.1f}')
