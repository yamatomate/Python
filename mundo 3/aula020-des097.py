# desafio 97 titulo que se ajusta ao tamanho da palavra
def escreva(pa="teste", ta=2):
    if type(ta) != int:
        ta = 1
    tama = ta * 2 + len(pa)
    print('=' * tama)
    print(" " * ta, end='')
    print(pa.capitalize())
    print('=' * tama)

escreva()
"""ppp = str(input("digite um titulo > "))
nnn = int(input("digite quanto quer sobresair > "))
escreva(pa=ppp, ta=nnn)"""
