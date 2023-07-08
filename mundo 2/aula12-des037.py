# desafio 37 conversão de um inteiro para binario octal e hexadecimal
num = int(input("digie um numero:"))
print("[1]converter para binario\n[2]converter para octal\n[3]converter para hexadecimal")
esc = int(input("escolha uma opção:"))
if esc == 1:
    num = bin(num)
    print(num[3:])
elif esc == 2:
    num = oct(num)
    print(num[2:])
elif esc == 3:
    num = hex(num)
    print(num[3:])
else:
    print("escolha invalida!")
