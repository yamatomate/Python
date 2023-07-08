x = 0
vez = int(int(input("tabuada do 1 ate quanto "))/2)
y = int(input("por quanto"))
for c in range(1, vez+1):
    x = x+1
    xa = x+vez
    mul = int(x*y)
    mul2 = int(xa*y)
    print(f'{x}x{y}={mul} | {xa}x{y}={mul2}')
print('='*20)
print('acabo')
