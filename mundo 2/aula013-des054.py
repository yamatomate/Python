# desafio 54 alistamento militar
from datetime import date
anot = date.today().year
mai = 0
mei = 0
for c in range(0, 7):
    ref = int(input('em que ano voce nasceu: '))
    ref = int(anot - ref)
    if ref >= 21:
        mai = mai + 1
    else:
        mei = mei + 1
    print('-'*6)
print(f'há {mai} acimda da maiorida e {mei} abaixo')
