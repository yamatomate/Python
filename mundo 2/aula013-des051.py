# desafio 51 programa de pa
inic = int(input('onde começa a sua PA: '))
raz = int(input('qual a razão da sua PA:'))
sopa = 0
pa = list()
pa = [inic]
for c in range(1, 10):
    sopa = pa[c-1] + raz
    pa.insert(c, sopa)
print(pa)
