# desafio 56 o homem mais velho e seu nome e qunatsa mulheres a baixo de 20
mns = 0
hmv = 0
hmvn = ''
med = 0
for c in range(0, 4):
    nome = str(input('qual seu nome:'))
    idade = int(input('qual a sua idade: '))
    med = med + idade
    sex = str(input('qual seu sexo [F|M]:')).upper()
    if sex == 'M' and idade > hmv:
        hmvn = nome
        hmv = idade
    if sex == "F" and idade < 20:
        mns = mns + 1
med = med/4
print(f'a media da idade do pessoal é igual a {med}, o nome do homem mais velho é {hmvn}', end=" ")
print(f' e a sua idade é {hmv}, e há {mns} muleres abaixo dos 20 anos')
