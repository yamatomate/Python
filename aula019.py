def soma(x, y):
    s = x + y
    print(s)
def contador(*num):
    for v in num:
        print(f"-> {v}")
def dobra(x):
    print(x)
    for c in range(0, len(x)):
        print(x[c], end=' -> ')
        x[c] *= 2
        print(x[c], end=';   ')


contador(4, 5, 32, 43, 4, "abacate")
soma(4, 5)
soma(8, 9)
soma(2, 1)
numeros = [4, 32, 23, 4, 54, 5]
dobra(numeros)
"""print("==="*10)
print("       GUSTAVO")
print("==="*10)

def linha():
    print("="*50)
def titulo(x):
    linha()
    print(f"{x:^50}")
    linha()

print()
linha()
print("       PRIMEIRA FUNÇAO")
linha()
print()
titulo("TIRUDJJUJD")"""
