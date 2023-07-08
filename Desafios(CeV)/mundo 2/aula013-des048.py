# desafio 48 soma entre todos os numeros impares multiplos de 3 entre 1 ate 500
soma = 0
"""para min surgiu 2 modos de fazer isso mas vou pegar o caminho mais facil
1 modo foi contar de 1 a 500 e se o numero da contagem ter uma resto igual a 1 na divisao com 2
e resto 0 em uma divisao com 3 ele somaria o numero
2 ate mais facil contar de 0 a 500 pulando em 3 e se o numero for impar some-o"""
for cont in range(0, 500, 3):
    if cont % 2 == 1:
        soma = soma + cont
        print(cont, end="; ")
print("")
print(soma)
