x = [2, 7, 9, 15]
z = 11
print(x, f"+ [{z}]")
print(len(x))
for c in range(0, len(x)):
    print(c, end=' ')
    if x[c - 1] < z < x[c]:
        x.insert(c, z)
        print('---')
        break
print(x)
