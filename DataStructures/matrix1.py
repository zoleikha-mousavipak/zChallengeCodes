A = [[1,3,5,7], [4,6,8,2], [5,7,9,3]]
print(A)
column = []
for row in A:
    print(row[0])
    column.append(row[2])

print(column)