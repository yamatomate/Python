listadenum = list(range(0, 15))
listadecoisas = ['carro', 'abacate', 'computador']
listona = list(listadenum + listadecoisas)
print(listadenum, "\n", listadecoisas, "\n", listona, "\n", "="*25)
del listadenum[6]
listadecoisas.insert(2, "memoria ram 8gb 3200hz kingstone por R$169,00")
listadenum.pop()
if "carro" in listadecoisas:
    listadecoisas.remove("carro")
print(listadenum, "\n", listadecoisas, "\n", listona)
