# desafio 27 primeiro e o ultimo nome de uma pessoa
nome = str('Gustavo lisboa oliveira')
nomesep = nome.split()
ultnom = int(len(nomesep)-1)
# print(nome, len(nomesep))
print(f'seu primeiro nome é {nomesep[0]} e o ultimo é {nomesep[ultnom]}')
