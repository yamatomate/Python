# 34 salario dos cara ae
sal = float(input('qual seu salario: '))
if sal >= 1250:
    novsal = (1250 * 1.15)
    print(f'seu novo salario {novsal:.2f}')
else:
    novsal = (1250 * 1.1)
    print(f'seu novo salario {novsal:.2f}')
print(sal, novsal, (novsal/1.15), (novsal/1.1))
