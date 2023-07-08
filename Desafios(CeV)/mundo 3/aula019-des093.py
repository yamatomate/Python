# desafio 93 analisando performace de um caba
dsp = {}
bb = "+=++"*5
dsp['Nome'] = str(input("Jogador: "))
pat = int(input("quantos jogos ele jogou: "))
dsp['gols'] = []
print(bb)
for c in range(0, pat):
    dsp['gols'].append(int(input(f'Quantos gols ele fez na partida {c+1}\': ')))
dsp['total'] = sum(dsp['gols'])
print(bb)
print(dsp)
print(bb)
for k, v in dsp.items():
    print(f"O campo {k} tem valor {v}")
print(bb)
print(f"o jogador {dsp['Nome']} jogou {pat} partidas:")
for c in range(0, pat):
    print(f"  --> Na partida {c+1}\' froam feito {dsp['gols'][c]} gols")
