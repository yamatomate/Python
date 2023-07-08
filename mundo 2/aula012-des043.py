# desafio 43 IMC
peso = float(input('qual seu peso: '))
altu = float(input('qual sua altura: '))
imc = peso/altu**2
if 18.5 < imc < 25:
    print("peso ideal")
elif 25 <= imc < 30:
    print("sobrepeso")
elif 30 <= imc < 40:
    print("obesidade")
elif imc < 18.5:
    print("abaixo do ideal")
else:
    print("nick avocado")
