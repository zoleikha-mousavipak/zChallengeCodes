def bubsort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




zarr = [9,5,1000,7,1,100,3,6,4,8,5,2,9,10]
print(bubsort(zarr))


#method2
# def bubsort(arr):
#     while True:
#         corrected = False
#         for i in range(0, len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 corrected = True
#         if not corrected:
#             return arr















