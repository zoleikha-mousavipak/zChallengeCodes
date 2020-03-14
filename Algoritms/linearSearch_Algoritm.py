def search(A,x):
    for i in range(len(A)):
        if A[i] == x:
            return i
        print(A[i])
    return -1


A = [2,8,555,7,1,100,3,6,4,8,5,2,9,10]
x = 555
print(search(A,x))