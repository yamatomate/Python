# desafio 95 analisando performace de um caba update
# !!!!! REFAZER !!!!!
jgds = []
while True:
    dsp = {}
    bb = "+=++" * 5
    dsp['Nome'] = str(input("Jogador: "))
    pat = int(input("quantos jogos ele jogou: "))
    dsp['gols'] = []
    dsp['total'] = 0
    print(bb)
    for c in range(0, pat):
        dsp['gols'].append(input(f'Quantos gols ele fez na partida {c + 1}\': '))
        dsp['total'] += int(dsp['gols'][c])
    print(bb)
    jgds.append(dsp.copy())
    rr = str(input("continuar [S\\N] >> "))
    if rr in "Nn0":
        break
print("==== " * 7)
print(f"  >cod e nome          >gols          >total")
for k in range(0, len(jgds)):
    print(f"  - {k}\'   {jgds[k]['Nome']} || {jgds[k]['gols']} || {jgds[k]['total']}")
