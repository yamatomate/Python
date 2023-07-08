# desafio 44 comprasss
pren = float(input("qual o preço original do profuto:"))
print(f"[1]A vista dinheiro/cheque\n[2]A vista no cartão")
opc = int(input("deseja usar qual opção:"))
if opc == 1:
    pren = pren * 0.9
    print(f"seu produto ganhou um desconto de 10%, pagará R${pren}")
elif opc == 2:
    opc = int(input("deseja parecelar em quantas vezes:"))
    if opc == 1:
        pren = pren * 0.95
        print(f"seu produto ganhou um desconto de 5%, pagará R${pren}")
    elif opc == 2:
        print(f"pagará R${pren}")
    else:
        pren = pren * 1.2
        print(f"pagará {pren} por {opc} meses")
