def aumentar(num, val, formt=True):
    num += val
    if formt:
        num = str(f"R$ {num:.2f}")
    return num
def diminuir(num, val, formt=True):
    num -= val
    if formt:
        num = str(f"R$ {num:.2f}")
    return num
def dobro(num, formt=True):
    num *= 2
    if formt:
        num = str(f"R$ {num:.2f}")
    return num
def metade(num, formt=True):
    num /= 2
    if formt:
        num = str(f"R$ {num:.2f}")
    return num
def resumo(nm, val1, val2):
    nm = int(nm)
    print("====="*7)
    print(f"{'RESUMO':^35}")
    print("====="*7)
    print(f"preço analisado:{' '*8}R$ {nm:.2f}")
    print(f"dobro do preço:{' '*9}R$ {dobro(nm, formt=False):.2f}")
    print(f"aumento {val1:>3}% do preço:{' '*2}R$ {nm*(1+(val1/100)):.2f}")
    print(f"redução {val2:>3}% do preço:{' '*2}R$ {nm*(1-(val2/100)):.2f}")