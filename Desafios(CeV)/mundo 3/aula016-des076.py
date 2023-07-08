# desafio 76 caixa de forma tabular
listdosuper = ["Pão", 1.00, "Tomate", 2.00, "Mortadela", 5.00, "Queijo Prato", 4.50, "Alface", 2.50, "Arroz", 10.00,
               "Feijão", 10.00, "Pernil de Porco", 25.00]
print('--'*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('--'*20)
cont = 0
while True:
    cot = cont + 1
    print(f'{listdosuper[cont]:.<30}', f'R${listdosuper[cot]:>7.2f}')
    if cot+1 == len(listdosuper):
        print('--' * 20)
        break
    else:
        cont += 2
