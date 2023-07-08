# desafio 114 verificando se pudim.com esta disponivel
import requests
try:
    servidor = requests.get('http://pudim.com.br')
    status = servidor.raise_for_status()
except:
    print("\033[0;31mNão é possivel acessar o site\033[0;0m")
else:
    print("\033[0;32mServidor acessivel\033[0;0m")