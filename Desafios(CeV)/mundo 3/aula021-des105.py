# desafio 105 funçao organizador de notas em dicionario
def notas(*num, sit=False):
    """ função que mostra um dicionario com informações sobre a notas da turma\n
    :*num: -> notas inteiras ou decimais\n
    :sit: -> entrada bool(), que diz sobre a situação da turma baseda na media
    de 0 a 5 é RUIM, de 5 ate 6 MEDIANA, 7 ate 10 OTIMA;\n
     True -> mostra no dicionario a situação\n
     False -> não mostra no dicionario a situação"""
    boletim = {}
    boletim['Quantidade'] = len(num)
    mm = num[0]
    mn = num[0]
    ss = 0
    for c in num:
        ss += c
        if c > mm:
            mm = c
        if c < mn:
            mn = c
    boletim['Maior'] = mm
    boletim['Menor'] = mn
    boletim['Media'] = ss/boletim['Quantidade']
    if sit:
        if boletim['Media'] < 5:
            boletim['Situação'] = "ruim"
        elif 5 <= boletim['Media'] < 7:
            boletim['Situação'] = "mediana"
        else:
            boletim['Situação'] = "ótima"

    print(boletim)




notas(4.5,3,7,6.7,8,10,6.5,4.5,sit=True)