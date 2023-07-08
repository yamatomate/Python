# desafio 92 carteria de trabalho
from datetime import datetime
ano = datetime.now().year
r = regis = {}
regis['Nome'] = str(input('Nome >> '))
regis['idade'] = int(ano - int(input('Ano de nascimento >> ')))
regis['CTPS'] = int(input('Carteira de trabalho (0 se não tiver )>> '))
if regis['CTPS'] != 0:
    regis['Ano de contratação'] = int(input('Ano de contratação >> '))
    regis['aposetadoria'] = r['idade'] + ((r['Ano de contratação'] + 35) - ano)
    regis['Salário'] = float(input('Salário >> R$'))
print('++=++'*5)
for k , v in regis.items():
    print(f'{k} = {v}')