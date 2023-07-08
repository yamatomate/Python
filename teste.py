# bloquinho de testes
"""x = 0
y = 5
vez = 5
print('='*20)
while x < vez:
    x = x+1
    xa = x+vez
    mul = int(x*y)
    mul2 = int(xa*y)
    print(f'{x}x{y}={mul} | {xa}x{y}={mul2}')
print('='*20)
print('acabo')"""
"""b = 5
h = 10
area = (b*h)/2
print(area)"""
"""def x():
    print('fodase')
x()"""
# umero decimal
num = 4
div = num
repi = 0
brio = ""
while not(div == 1):
    repi = repi + 1
    brio = brio+str((div % 2))
    div = div//2
    # print(f"{brio} binario, vezes {repi} ,{div}")
brio = str(brio)+str(div)
print(brio[::-1], " = ", num)


div = num
repi = 0
octa = ""
while not(div == 0):
    repi = repi + 1
    octa = octa+str((div % 8))
    div = div//8
    # print(f"{octa} octa, vezes {repi} ,{div}")
octa = str(octa)
print(octa[::-1], " = ", num)

div = num
repi = 0
hexade = ""
while not(div == 0):
    repi = repi + 1
    hexade = hexade + str((div % 16))
    div = div // 16
    # print(f"{hexade} hexa, vezes {repi} ,{div}")
hexade = str(hexade)
print(hexade[::-1], " = ", num)
"""
print('sopa de macaco'.upper)"""