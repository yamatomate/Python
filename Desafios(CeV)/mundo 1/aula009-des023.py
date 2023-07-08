# desafio 23 0 a 9999
from random import randint
num = randint(0, 9999)
"""num = int(input('de 0 a 9999 digite um numero: '))
num = """
numt = str(num+10000)
"""resolução do guanabara num//1%10 ex: 1834//1 -> 1834%10 -> 4 """
print(f'o seu numero {num}\nmilhar:{numt[1]}\ncentena:{numt[2]}')
print(f'dezena:{numt[3]}\nunidade:{numt[4]}')
