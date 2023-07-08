# emprestimo para compra de casa
print("|", "-=-"*5, "|")
print("|   Emprestimo    |")
print("|", "-=-"*5, "|")
sal = float(input("qual o seu salario:"))
caspre = float(input("qual o preço da casa:"))
temp = int(input("por quantos anos vai pagar:"))
pretmen = (caspre/(temp*12))
if pretmen <= sal * 0.3:
    print("emprestimo aceito seja feliz com sua nova residencia")
else:
    print("emprestimo negado! tenha um bom dia")
# print(f"sal={sal},preço={caspre},tempo={temp},preço por mes={pretmen}")
# print(f"30% do sala={sal * 0.3}, condição={(pretmen <= sal * 0.3)}")
