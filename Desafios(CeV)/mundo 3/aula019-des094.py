# desafio 94 contratacção de varios caba
"""A) quantas pessoas cadastradas
B) A media de idade do grupo 
C) uma lista so com mulheres
D) uma lista com todas as pessoas com idade acima da media"""
galera = []
pessoa = {}
pp = "==== " * 7
soma = 0
while True:
    print(pp)
    pessoa.clear()
    pessoa['Nome'] = str(input("digite seu nome >> "))
    while True:
        pessoa['Sexo'] = str(input("digite seu sexo [M\\F] >> "))
        if pessoa['Sexo'] in "MmFf":
            break
        print("--Opção invalida--")
    pessoa['Idade'] = int(input("Digite a sua idade >> "))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    print(pp)
    while True:
        rr = str(input("deseja continuar [S\\N] >> "))
        if rr in "NnSs01":
            break
    if rr in "Nn0":
        break
media = soma / len(galera)
print("==+++==" * 6)
print(f"Foram registrado {len(galera)} pessoas")
print(f"Média é igual a {media:.2f}")
print(f"Apenas as mulheres:")
for p in galera:
    if p['Sexo'] in "Ff":
        print(f"{p['Nome']};   ", end='')
print('')
print("Pessoal que esta acima da media:")
for p in galera:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f"-->{k} é igual a {v}   ", end='')
        print(';')
