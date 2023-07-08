def leiaInt(text="Digite um numero inteiro: ", seleto=False, grupo=[]):
    """leiaint é um comando que le um número inteiro para o usuario.\n
    >> esse comando retorna valor <<\n
    parametros:\n
    - text -> é a mensagem que vai aparecer na entrada do valor"""
    while True:
        try:
            num = int(input(text))
            if seleto:
                if num not in grupo:
                    print("\033[0;31mDigite um numero valido.\033[;;m")
                    continue
        except:
            print("\033[0;31mError >> digite um numero inteiro valido.\033[;;m")
            continue
        else:
            return num

def leiaFloat(text="Digite um numero real: "):
    """leiaFloat é um comando que le um número real para o usuario.\n
    >> esse comando retorna valor <<\n
    parametros:\n
    - text -> é a mensagem que vai aparecer na entrada do valor"""
    while True:
        try:
            num = float(input(text))
        except:
            print("\033[0;31mError >> digite um numero real valido.\033[;;m")
            continue
        else:
            return num
