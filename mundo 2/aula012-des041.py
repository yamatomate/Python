# desafio 41 classficando nadadores
from datetime import datetime
ano = datetime.now()
anonsc = int(input("em que ano voce nasceu:"))
idade = ano.year - anonsc
if idade < 9:
    print("nadador mirin")
elif 9 <= idade < 14:
    print("nadador infatil")
elif 14 <= idade <= 19:
    print("nadador junior")
elif idade == 20:
    print("nadador sênior")
else:
    print("nadador master")
print(idade)
