# desafio 89 programinha que mostra o boletim
aluno = []
banco = ba = []
while True:
    aluno.append(str(input("Digite o nome do aluno: ")))
    aluno.append(float(input("Digite a primeira nota: ")))
    aluno.append(float(input("Digite a segunda nota: ")))
    banco.append(aluno[:])
    aluno.clear()
    rr = str(input("> Deseja continuar [S|N] - "))
    if rr not in "Ss1":
        break
    print('==='*5, 'botelim coletado!')
for c in range(0, len(ba)):
    ba[c].append( (ba[c][1]+ba[c][2])/2 )

rr = "SIM"

while True:
    if rr in "SIM":
        print('==='*5,'\nMedia da turma')
        for c in range(0, len(ba)):
            print(f'Aluno N.{c} - {ba[c][3]}')
    elif rr == "SAIR" or rr in "NN":
        print("fechando...")
        break
    else:
        print('comando invalido')
    rr = str(input("\n(para sair digite \'sair\')\n> Digite o N. do aluno para ver suas notas - ")).upper().strip()
    if rr.isnumeric():
        rr = int(rr)
        print('==='*5)
        print(f'Aluno: {ba[rr][0]}\nnotas:  P1 = {ba[rr][1]}  P2 = {ba[rr][2]}\n')
        rr = str(input("(para sair digite \'sair\')\n> Voltar para boletim geral? - ")).upper().strip()
        