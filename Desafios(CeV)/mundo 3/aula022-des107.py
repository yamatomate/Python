# desafio 107 modulo mueda
import moeda

x = int(input("digite um valor >> "))
print(f"{x} + 25 = {moeda.aumentar(x, 25)}\n{x} - 25 = {moeda.diminuir(x, 25)}\n{x} * 2 = {moeda.dobro(x)}\n{x} / 2 = {moeda.metade(x)}")