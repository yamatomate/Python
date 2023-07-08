# desafio 103 ficha de um jogador
def ficha(nome, gol):
    if nome in "":
        nome= str(">Desconhecido<")
    if str(gol).isnumeric():
        int(gol)
    print(f"O jogador {nome.capitalize()}, fez {gol} gols.")

x = str(input("Nome:"))
y = str(input("gols:"))
ficha(x, y)
