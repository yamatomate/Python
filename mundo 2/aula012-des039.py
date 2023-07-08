# deasfio 39 sera que u mininu ja tem que ir para o exercito
anoat = 2023
# anodn = int(input("em que ano vc nascue: "))
anodn = 2008
idade = anoat - anodn
if idade == 18:
    print("ja esta na hora de se alistar")
elif idade > 18:
    print(f"ta podi ja passou da validade faz {idade-18} ano nem faculdade vai mais fazer tadin")
else:
    print(f"ainda nao esta na idade de servir, pois falta {18-idade} ano")
