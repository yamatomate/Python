# desafio 115 lista que salva nome e idade das pessoas
import aula23.leiadado as leiadado
from time import sleep

def add_pessoa(nome, idade):
    with open('pessoas.txt', 'a') as arquivos:
        arquivos.write(f"nome: {nome} - idade: {idade}\n")
def reset_pessoa():
    with open('pessoas.txt', 'w') as arquivos:
        arquivos.write("")
def list_pessoa():
    print("============================\n")
    with open('pessoas.txt', 'r') as arquivos:
        for c in arquivos:
            print(f" -> {c}")
        print("")
def escreva(pa="teste", ta=2):
    """veio da aula020-des097.py não consegui importar"""
    if type(ta) != int:
        ta = 1
    tama = ta * 2 + len(pa)
    print('=' * tama)
    print(" " * ta, end='')
    print(pa.capitalize())
    print('=' * tama)

# programa principal

while True:
    escreva("Lista dos caloterios", 4)
    sleep(0.3)
    print("  1 -> adicionar pessoa\n  2 -> listar pessoas\n  3 -> sair")
    rr = leiadado.leiaInt("  escolha uma opção >> ",seleto=True,grupo=[1,2,3,5])
    print("  ", end='')
    for c in range(0, 3):
        print(".", end='', flush=True)
        sleep(0.3)
    print(" feito!")
    if rr == 1:
        nm = str(input("Qual o nome da pessoa: "))
        ida = leiadado.leiaInt("Qual a idade dela: ")
        add_pessoa(nm, ida)
    elif rr == 2:
        list_pessoa()
    elif rr == 3:
        break
    elif rr == 5:
        reset_pessoa()
print("confira sempre!")