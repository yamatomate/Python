# desafio 23 sera que começa com santa
"""cid = str(input('qual nome da sua cidade: ')"""
cid = str('  SobRAl         ').strip()
cidt = cid.upper()
elemcid = cidt.split()
temoun = bool(elemcid[0].find('SANTA')+1)
# print(cid, elemcid, elemcid[0].find('SANTA')+1)
print(f'sua cidade, {cid} dá {temoun} por começar com Santa ')
