A = int(input("input: "))
j = []
res = []
k = []
for i in range(A, 0, -1):
    j = j + ([i] * i)
    j = j + j[-2::-1]
    res.append(j)
    k.append(i)
    j = k.copy()
res.extend(res[-2::-1])
print(res)