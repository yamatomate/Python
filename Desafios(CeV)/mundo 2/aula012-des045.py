# desafio 45 jogo do pedra papel tesoura
from random import choice
pe = "PEDRA"
pa = "PAPEL"
te = "TESOURA"
print("pedra papel e tesoura, escolha um")
jg = str(input(">")).upper()
kri = choice([pe, pa, te])
if jg == kri:
    print(f"{jg.lower()} X {kri.lower()} empate")
elif jg == pe and kri == pa:
    print(f"{jg.lower()} X {kri.lower()} ; {pa.lower()} ganha")
elif jg == pe and kri == te:
    print(f"{jg.lower()} X {kri.lower()} ; {pe.lower()} ganha")
elif jg == pa and kri == te:
    print(f"{jg.lower()} X {kri.lower()} ; {te.lower()} ganha")
elif jg == pa and kri == pe:
    print(f"{jg.lower()} X {kri.lower()} ; {pa.lower()} ganha")
elif jg == te and kri == pe:
    print(f"{jg.lower()} X {kri.lower()} ; {pe.lower()} ganha")
elif jg == te and kri == pa:
    print(f"{jg.lower()} X {kri.lower()} ; {pa.lower()} ganha")
