# desafio 73 nomes de coisas rankeadas
redstone = ("bloco de redstone", "redstone", "pistão", "pistão com slime", "bloco de slime", "palca de pressão",
            "botão", "alavanca", "tocha de redstone", "repetidor", "comparador", "ejetor", "disparador")
print('--> Os primeiros 5 colocados são: ')
for c in range(0, 5):
    print(f' {c+1}\' {redstone[c]}')
print('--> Os ultimos 4 colocados:')
x = len(redstone)
for c in range((x-4), x):
    print(f' {c}\' {redstone[c]}')
print('--> Em ordem alfabetica fica:')
x = sorted(redstone)
for c in range(0, (len(redstone))):
    print(f' -{x[c]}')
print(f'--> A redstone fica na posição:')
c = 0
while True:
    x = "redstone"
    if redstone[c] == x:
        print(f' {c+1}\' \"{x}\"')
        break
    c += 1
    if c == len(redstone):
        print(' -não encotrado')
        break
