# faça um programa que leia o nome e o peso de varias pessoas
print("--hospital do peso--")
pe = []
while True:
    pe.append(str(input("digite seu nome >> ")))
    pe.append(int(input("digite seu peso >> ")))
    rr = str(input("continuar [s\\n] >>"))
    if rr in "Nn0":
        print("==="*10)
        break
    else:
        print("==="*10, " dado guardado")
print(pe)
ma = pe[1]
me = pe[1]
#print(ma, "   ", me)
for c in range(1, len(pe),2):
    if pe[c] > ma:
        ma = pe[c]
    if pe[c] < me:
        me = pe[c]
    #print(ma, "   ", me)
print("O resultado da pesquisa:")
print(f"- {len(pe)} pessoas participaram da pesquisa")
print(f"- {ma}Kg foi o maior peso:")
for c in range(1, len(pe),2):
    if pe[c] == ma:
        print(" ", pe[c-1])
print(f"- {me}Kg foi o menor peso:")
for c in range(1, len(pe),2):
    if pe[c] == me:
        print(" ", pe[c-1])
        