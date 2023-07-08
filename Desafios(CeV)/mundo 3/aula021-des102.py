# desafio 102 faça um fatorial função, esse foi mt facil ate pq ja tava feito na aula
def fatorial(x=1, show=False):
    """:x: inteiro que recebe o numero que sera fatoriado
    :modo: caso o modo seja = 0 ele apennas imprimirar o fatorial
    caso o modo seja = 1 ele retornara o resultado do fatorial
    """
    fat = 1
    if show:
        print(f"{x}! --> ", end='')
        for c in range(x, 0, -1):
            if c != 1:
                print(f"{c}x", end='')
                fat *= c
            else:
                print(f"{c}={fat}")
    else:
        for c in range(x, 1, -1):
            fat *= c
        print(fat)


fatorial(7)
print(fatorial(7,show=True))