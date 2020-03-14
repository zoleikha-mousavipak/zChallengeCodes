def insertion_sort(A):
    for i in range(1, len(A)):
        j = i-1
        while A[j] > A[j+1] and j>=0:
            A[j],A[j+1] = A[j+1],A[j]
            j -= 1
    return A


zarr = [2,8,555,7,1,100,3,6,4,8,5,2,9,10]
print(insertion_sort(zarr))
