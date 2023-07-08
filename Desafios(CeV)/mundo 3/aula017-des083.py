# desafio 83 confirmação se uma expresao com ( ) é possivel
exp = str(input('Digite a sua expressão ->> '))
pd = exp.count('(')
pe = exp.count(')')
print(exp not in '()')
if pd - pe == 0:
    print(f'A sua expressão {exp} é possivel, não há parenteses aberto')
elif pd - pe != 0:
    print(f'A sua expressão {exp} NÃO é possivel, há parenteses aberto')
