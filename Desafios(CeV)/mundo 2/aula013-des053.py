# desafio 53 leitor de palavras polindromas
pu = str(input('digite uma palavra ou frase: '))
pal = pu.upper()
pal = pal.replace(' ', '')
# pal = str('eevee')
poli = True
for c in range(0, len(pal)):
    if pal[c] != pal[-c-1]:
        poli = False
    """print(c, pal[c], pal[-c-1])
    if pal[c] == pal[-c-1]:
        print(pal[c])
    else:
        poli = False"""
# print(len(pal), poli, pal)
if poli:
    print(f'A sua palavra ou frase "{pu}" é um polidromio')
else:
    print(f'A sua palavra ou frase "{pu}" NÃO é um polidromio')
