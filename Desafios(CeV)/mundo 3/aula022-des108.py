# desafio 108 mesmo do anteiro porem com formatação R$ 0,00

import moeda

x = int(input("digite um valor >> "))
print(f"""{x} + 25 = {moeda.aumentar(x, 25)}
{x} - 25 = {moeda.diminuir(x, 25)}
{x} * 2 = {moeda.dobro(x)}
{x} / 2 = {moeda.metade(x)}""")