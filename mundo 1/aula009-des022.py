# desafio 22 analisador de nome
"""nome = str(input('digite seu nome completo: ')"""
nome = str('marilha da silva mença')
nome = nome.strip()
senome = nome.replace(' ', '')
sepnome = nome.split()
# print(nome, len(senome), len(sepnome[0]))
print(f'{nome.upper()}\n{nome.title()}\nao todo seu nome tem {len(senome)+1}', end=' ')
print(f'seu primeiro nome tem {len(sepnome[0])} letras')
