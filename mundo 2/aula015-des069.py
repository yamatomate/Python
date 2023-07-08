# desafio 69 leia um monte de dados
"""quantos tinham mais de 18 , quantos homens e quantas mulheres com menos de 20 anos"""
ac = 0  # total acima dos 18
hh = 0  # total de homens
mn = 0  # mulheres com menos de 20
while True:
    gg = " "
    cc = " "
    idade = int(input('Qual a sua idade >> '))
    while gg not in "HM":
        gg = str(input('Qual seu sexo [H/M] >> ')).upper().strip()

    while cc not in 'SN':
        cc = str(input('Deseja continuar [S/N] >> ')).upper().strip()

    if idade >= 18:
        ac += 1

    if gg == "H":
        hh += 1
    elif gg == "M" and idade < 20:
        mn += 1

    if cc == "N":
        print('=' * 20)
        break
    print('='*20)
print(' |fim da coleta|')
print(f"""Feita a coleta é costatado que:\n-há {ac} pessoas acima dos 18 anos\n-há {hh} homens
-há {mn} mulheres abaixo dos 20 anos""")
