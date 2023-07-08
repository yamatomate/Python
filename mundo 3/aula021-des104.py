# desafio 104 funçao leiaint parceido com input
def leiaint(text):
    while True:
        x = str(input(text)).strip()
        if x.isnumeric():
            x = int(x)
            return x
        print(f">{x}< não é um numero inteiro, tente novamente.")


abacate = leiaint("Digite um numero >> ")
print(abacate)