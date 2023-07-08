# desafio 111 pacote de modulos
import utilidades_des.moeda
import utilidades_des.dado
moeda = utilidades_des.moeda
dado = utilidades_des.dado
x = dado.leiaint("Digite um valor >> R$")
y = dado.leiaint("Digite o aumento % >> ")
z = dado.leiaint("Digite a redução % >> ")
moeda.resumo(x,y,z)