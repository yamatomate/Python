# desafio 101 funça sera que ta na idade de votar
def Vote():
    from datetime import datetime
    i = idade = datetime.now().year - int(input("Em que ano voce nasceu >> "))
    if i < 16:
        i = "Negada"
    elif 16 <= i < 18:
        i = "Opcional"
    elif 18 <= i <= 65:
        i = "Obrigatorio"
    else:
        i = "Opcional"
    return i

condi = Vote()
print(f"Seu valor para votar é {condi}")
