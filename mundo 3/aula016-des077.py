# desafio 77 tuplas com palavras e suas vogais
tutu = ["otorrinolaringologista", "milho", "biomancia", "batata", "rynjas", "suco de limonatios"]
vogais = ["a", "e", "i", "o", "u"]

for cont in range(0, len(tutu)):
    pal = tutu[cont]
    print(f'{pal} - ', end="")
    for c in range(0, len(pal)):
        if pal[c] in vogais:
            print(pal[c], end=' ')
    print('')
