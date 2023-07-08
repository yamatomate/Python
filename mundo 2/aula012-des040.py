# desafio 40 sera que a media desse maluco ta boa
nt1 = float(input("qual foi a sua primeira nota: "))
nt2 = float(input("qual foi a sua segunda nota: "))
med = (nt1 + nt2)/2
if med > 5:
    print("reprovado")
elif 6.9 > med > 5:
    print("recuperação")
else:
    print("o mininu bom passou")
