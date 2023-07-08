# aula 10 condicionais
"""tempo = int(input('quantos anos tem seu carro: '))
if tempo <= 3:
    print('carro novo, mt é massa')
else:
    print('carro vei, mt é paia')"""
# exemplo 1;
"""nome = str(input('qual seu nome? '))
if nome == 'gustavo':
    print('nome lindão tu é doido')
else:
    print('nome paia teu')
print(f'bom dia, {nome}')"""
# exemplo 2 (classico);
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
med = (nota1+nota2)/2
print(f'a sua media é igual a {med:.1f}', end=' ')
if med >= 6:
    print('parabens sua media foi acima de 6')
else:
    print('boa ta reprovado seu fudido nunca vai ser alguem na vida se tirar nota baixa assim')
