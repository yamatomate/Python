def leiaint(text=str()):
    """enquanto a respota não for igual a um numero
    ficará em um loop
    :text: STR -> o texto desginada para pergunta ou que seja"""
    while True:
        x = str(input(text)).strip()
        if x.isnumeric():
            x = int(x)
            return x
        print(f">{x}< não é um numero inteiro, tente novamente.")
        
def leiameoda(text=str()):
    """enquanto a respota não for igual a um numero
    ficará em um loop
    :text: STR -> o texto desginada para pergunta ou que seja"""
    while True:
        x = str(input(text)).strip()
        if x.isnumeric():
            x = float(x)
            return x
        print(f">{x}< não é um numero inteiro, tente novamente.")