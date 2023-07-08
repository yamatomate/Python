def fatorial(x=1, modo=0):
    """:x: inteiro que recebe o numero que sera fatoriado
    :modo: caso o modo seja = 0 ele apennas imprimirar o fatorial
    caso o modo seja = 1 ele retornara o resultado do fatorial
    """
    fat = 1
    if modo == 0:
        print(f"{x}! --> ", end='')
        for c in range(x, 0, -1):
            if c != 1:
                print(f"{c}x", end='')
                fat *= c
            else:
                print(f"{c}={fat}")
    elif modo == 1:
        for c in range(x, 1, -1):
            fat *= c
        return fat


fatorial(2, modo=0)
print(fatorial(7,modo=1))