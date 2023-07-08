# desafio 26 a cada dia mais insanom -procure os A em uma frase-
# frase = str(input('digite uma frase que conatremos os A : '))
frase = str('Arara azul').strip().upper()
qafr = frase.count('A')
cad1 = frase.find('A')+1
cad2 = frase.rfind('A')+1
# print(qafr, cad1, cad2)
print(f'a quantidade de A na sua frase é: {qafr}\nprimeira vez que aperece é: {cad1}')
print(f'e a ultima é: {cad2}')
